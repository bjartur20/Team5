import requests

def get_user(api_url, username):
    session = requests.Session()

    r = session.get(api_url + 'user/')
    
    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None
    
    users = r.json()

    for user in users:
        if user['username'] == username:
            return user

    print('Cannot find user')
    return None

def get_user_id(api_url, user_id):
    session = requests.Session()

    r = session.get(api_url + 'user/' + user_id)

    if r.status_code != 200:
        print('Cannot connect to API:', r.status_code)
        return None
    
    return r.json()['user_id']

def save_user(api_url, user):
    session = requests.Session()

    r = session.post(api_url + 'user', data=user)
    
    if r.status_code != 200:
        return f'Cannot connect to API {r.status_code}'