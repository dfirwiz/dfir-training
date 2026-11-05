"""Compare fictional event-time intervals; neither causation nor real incident analysis."""
import argparse
from datetime import datetime, timedelta, timezone
import json
import math
from pathlib import Path


def compare(data, left='vpn', right='endpoint', extra=0):
    if isinstance(extra,bool) or not isinstance(extra,(int,float)) or not math.isfinite(extra) or extra<0:
        raise ValueError('extra uncertainty must be finite and non-negative')
    if not isinstance(data,dict) or data.get('schema')!='training-time-v1' or not isinstance(data.get('events'),list) or not data['events']:
        raise ValueError('non-empty training-time-v1 events required')
    rows={}
    for e in data['events']:
        if not isinstance(e,dict) or any(not isinstance(e.get(k),str) or not e[k] for k in ('id','source','event_time','kind')):
            raise ValueError('event id, source, time and kind required')
        if e['id'] in rows:raise ValueError('duplicate event id')
        t=datetime.fromisoformat(e['event_time'].replace('Z','+00:00'))
        if t.tzinfo is None or t.utcoffset() is None:raise ValueError('timezone required')
        t=t.astimezone(timezone.utc)
        u=e['uncertainty_seconds']
        if isinstance(u,bool) or not isinstance(u,(int,float)) or not math.isfinite(u) or u<0:
            raise ValueError('finite non-negative uncertainty required')
        width=timedelta(seconds=u+extra)
        rows[e['id']]=(t,t-width,t+width,e)
    if left not in rows or right not in rows:raise ValueError('unknown event id')
    a,b=rows[left],rows[right]
    relation='left_before_right' if a[2]<b[1] else 'left_after_right' if a[1]>b[2] else 'order_not_resolved'
    def interval(x):return dict(source=x[3]['source'],kind=x[3]['kind'],earliest=x[1].isoformat(),latest=x[2].isoformat())
    return dict(status='interval_comparison_only',left=interval(a),right=interval(b),nominal_delta_seconds=(b[0]-a[0]).total_seconds(),relation=relation,causation='not_tested',real_incident='not_analyzed',external_actions=0)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('file',type=Path)
    p.add_argument('--left',default='vpn');p.add_argument('--right',default='endpoint')
    p.add_argument('--extra-uncertainty-seconds',type=float,default=0)
    a=p.parse_args()
    try:
        print(json.dumps(compare(json.loads(a.file.read_text(encoding='utf-8')),a.left,a.right,a.extra_uncertainty_seconds),indent=2))
        return 0
    except (OSError,ValueError,KeyError,TypeError,OverflowError) as exc:
        print('ERROR '+str(exc));return 2


if __name__=='__main__':raise SystemExit(main())
