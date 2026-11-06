"""Compute harmless byte examples only; decoded bytes are never executed."""
import base64,json
from urllib.parse import unquote,unquote_plus,urlsplit

def explore():
    examples=[]
    for raw in [b'A',b'AB',b'ABC',b'ABCD',bytes([251,255])]:
        standard=base64.b64encode(raw).decode();safe=base64.urlsafe_b64encode(raw).decode()
        examples.append(dict(raw_hex=raw.hex(),bytes=len(raw),standard=standard,url_safe=safe,length=len(standard)))
    errors={}
    for text in ['QUI','QUI=!', 'QUI=\n']:
        try:base64.b64decode(text,validate=True);errors[text]='accepted'
        except ValueError:errors[text]='rejected'
    return dict(examples=examples,strict_errors=errors,percent_once=unquote('QUI%3D'),plus_url=unquote('+w=='),plus_form=unquote_plus('+w=='),host=urlsplit('https://files.example/report?token=TRAINING').hostname,external_actions=0)
if __name__=='__main__':print(json.dumps(explore(),indent=2))
