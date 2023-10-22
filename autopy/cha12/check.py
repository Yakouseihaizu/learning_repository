import requests as rqs

res = rqs.get('https://inv.com/not_exits')
try:
    res.raise_for_status()
except rqs.HTTPError as exc:
    print('There was a problem: '+str(exc))
    
