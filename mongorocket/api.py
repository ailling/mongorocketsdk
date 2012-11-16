
import warnings

try:
    import settings
except Exception:
    settings = None
    warnings.warn('No settings.py found on your project path. It is recommended to set API credentials in settings.py located ath the root of your project directory')


import requests
import json

SAVE_URL = 'http://api.botrocket.com/v1/data/save/'
#SAVE_URL = 'http://localhost:8000/v1/data/save/'

def get_cred(name, default, required=False):
    if default:
        return default
    if settings and getattr(settings, name, ''):
        return getattr(settings, name)
    else:
        if required:
            raise Exception('Failed to find %s as parameter or in settings.py' % name)
    return ''



def save(collection, data={}, no_duplicates=False,
         username='', client_key='', database=''):
    
    if not data:
        return False
    
    username = get_cred('USERNAME', username)
    client_key = get_cred('CLIENT_KEY', client_key)
    database = get_cred('DATABASE', database, required=True)
    
    payload = {'client_key': client_key,
        'username': username,
        'database': database,
        'collection': collection,
        'no_duplicates': no_duplicates,
        'data': json.dumps(data)
    }
    
    resp = requests.post(SAVE_URL, data=payload)
    
    reply = json.loads(resp.text)
    
    return reply['status'] == 'OK'


