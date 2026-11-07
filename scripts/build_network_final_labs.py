"""Create fictional local visibility and mail fixtures, never contact a network."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]/'assets/network-security'
def build():
 def stamp(m):return f'2026-11-07T09:{m:02d}:00+00:00'
 sensors={'mail':dict(path='mail-edge',kinds=['smtp_accept'],start=stamp(0),end=stamp(30)), 'dns':dict(path='client-resolver',kinds=['dns_query'],start=stamp(0),end=stamp(30)), 'border':dict(path='client-outside',kinds=['tls_flow','outbound_bytes'],start=stamp(0),end=stamp(30)), 'east':dict(path='client-server',kinds=['smb_flow'],start=stamp(0),end=stamp(30))}
 stage_defs=[('S1','mail-edge',['smtp_accept']),('S2','client-resolver',['dns_query']),('S3','client-outside',['tls_flow']),('S4','client-server',['endpoint_process']),('S5','client-server',['server_file_write']),('S6','client-outside',['outbound_bytes','file_identity'])]
 stages=[dict(id=i,path=path,required=k,start=stamp(0),end=stamp(30)) for i,path,k in stage_defs]
 records=[dict(id='R1',sensor='mail',path='mail-edge',kind='smtp_accept',time=stamp(1)),dict(id='R2',sensor='dns',path='client-resolver',kind='dns_query',time=stamp(2)),dict(id='R3',sensor='border',path='client-outside',kind='tls_flow',time=stamp(3)),dict(id='R4',sensor='east',path='client-server',kind='smb_flow',time=stamp(5)),dict(id='R5',sensor='border',path='client-outside',kind='outbound_bytes',time=stamp(8))]
 p=ROOT/'day02-lab23';p.mkdir(exist_ok=True);(p/'cases.json').write_text(json.dumps(dict(schema='training-visibility-v1',external_actions_allowed=False,sensors=sensors,stages=stages,records=records),indent=2)+'\n',encoding='utf-8')
 p=ROOT/'day02-lab24';p.mkdir(exist_ok=True);files={}
 for name,author,known in [('message-a.eml','Training Helpdesk <helpdesk@example.org>',True),('message-b.eml','Training Executive <chief@example.org>',False)]:
  lines=['X-Training-Only: true','Return-Path: <bounce@mailer.example.net>','Received: from mx.receiver.example (mx.receiver.example [203.0.113.10])',' by store.receiver.example with ESMTP id STORE-TRAIN;',' Sat, 07 Nov 2026 09:00:04 +0000','Received: from outbound.example.net (outbound.example.net [198.51.100.40])',' by mx.receiver.example with ESMTP id EDGE-TRAIN;',' Sat, 07 Nov 2026 20:00:00 +1100','Authentication-Results: mx.receiver.example;',' spf=pass smtp.mailfrom=bounce@mailer.example.net;',' dkim=pass header.d=example.org','Authentication-Results: outside.example.net;',' spf=pass smtp.mailfrom=pretend@example.org;',' dkim=pass header.d=example.org',f'From: {author}','To: Analyst <analyst@receiver.example>','Date: Sat, 07 Nov 2026 19:59:57 +1100',f'Message-ID: <{name}@training.example>','Subject: Fictional training notice','MIME-Version: 1.0','Content-Type: text/plain; charset=us-ascii','','Training notice only. Do not open links.','https://portal.example.org/training','']
  raw='\r\n'.join(lines).encode('ascii');(p/name).write_bytes(raw)
  files[name]=dict(sha256=hashlib.sha256(raw).hexdigest(),ar_index=0,expected_authserv_id='mx.receiver.example',receiver_provenance_claim=known,smtp_data_accepted_claim=True)
 (p/'context.json').write_text(json.dumps(dict(schema='training-email-evidence-v1',external_actions_allowed=False,files=files),indent=2)+'\n',encoding='utf-8');print('Created fictional JSON and2CRLF EML files; no network activity.')
if __name__=='__main__':build()
