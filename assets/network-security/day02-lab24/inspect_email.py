"""Inspect fixed fictional EML/header-result claims; no DNS, SMTP or crypto verification."""
from pathlib import Path
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses,parsedate_to_datetime
import argparse,json,re,hashlib
def domain(value):
 if value.count('@')!=1:raise ValueError('fixed mailbox form required')
 s=value.rsplit('@',1)[1].lower()
 if not re.fullmatch(r'[a-z0-9]+(?:[.-][a-z0-9]+)*',s):raise ValueError('ASCII teaching domain required')
 return s
def inspect(path,ctx):
 raw=Path(path).read_bytes()
 if hashlib.sha256(raw).hexdigest()!=ctx['sha256']:raise ValueError('context-to-file hash mismatch')
 msg=BytesParser(policy=policy.default).parsebytes(raw)
 if msg.defects or len(msg.get_all('From',[]))!=1:raise ValueError('one well-formed From required')
 addresses=getaddresses([str(msg['From'])])
 if len(addresses)!=1:raise ValueError('one author mailbox subset')
 author=domain(addresses[0][1]);ar=msg.get_all('Authentication-Results',[]);i=ctx['ar_index']
 if type(i) is not int or not 0<=i<len(ar):raise ValueError('explicit existing header index required')
 selected=str(ar[i]);authserv=selected.split(';',1)[0].strip();match=re.fullmatch(r'([^;]+);\s*spf=(pass|fail|none) smtp.mailfrom=([^;\s]+);\s*dkim=(pass|fail|none) header.d=([^;\s]+)',selected)
 if not match:raise ValueError('fixed one-SPF-one-DKIM report subset')
 _,spf,mailbox,dkim,signer=match.groups();envelope=domain(mailbox);signer=signer.lower()
 for key in ('receiver_provenance_claim','smtp_data_accepted_claim'):
  if type(ctx[key]) is not bool:raise ValueError('explicit context booleans required')
 usable=ctx['receiver_provenance_claim'] and authserv==ctx['expected_authserv_id']
 aligned=((spf=='pass' and envelope==author) or (dkim=='pass' and signer==author)) if usable else None
 times=[]
 for received in msg.get_all('Received',[]):
  t=parsedate_to_datetime(str(received).rsplit(';',1)[1].strip())
  if t.utcoffset() is None:raise ValueError('Received timezone required')
  times.append(t)
 if len(times)!=2:raise ValueError('fixed two-Received subset')
 return dict(file=Path(path).name,sha256=hashlib.sha256(raw).hexdigest(),author_domain=author,selected_authserv_id=authserv,selected_header_index=i,reported_spf=spf,reported_spf_domain=envelope,reported_dkim=dkim,reported_signing_domain=signer,report_usable_under_context_claim=usable,strict_alignment_from_report_claims=aligned,received_time_difference_seconds=(times[0]-times[1]).total_seconds(),smtp_data_accepted_claim=ctx['smtp_data_accepted_claim'],attachment_count=sum(1 for x in msg.walk() if x.get_content_disposition()=='attachment'),actual_dns_checked=False,actual_dkim_signature_verified=False,actual_receiver_provenance_verified=False,actual_smtp_or_mailbox_delivery_verified=False,actual_user_action_verified=False,incident_verdict='unresolved',external_actions=0)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('eml',type=Path);p.add_argument('context',type=Path);a=p.parse_args()
 try:
  d=json.loads(a.context.read_text(encoding='utf-8'))
  if d.get('schema')!='training-email-evidence-v1' or d.get('external_actions_allowed') is not False:raise ValueError('teaching contract required')
  print(json.dumps(inspect(a.eml,d['files'][a.eml.name]),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError,IndexError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
