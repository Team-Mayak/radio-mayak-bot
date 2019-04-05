AUTH = False # change to True if proxy needs a username and a password to use
TOKEN = '' # paste the token here
PROXY = 'https://208.88.233.1:54149' # this proxy address may be changed
USERNAME = '' # username if authentication is needed
PASSWORD = '' # password if required
if not AUTH:
    REQUEST_KWARGS = {'proxy_url': PROXY}
else:
    REQUEST_KWARGS = {'proxy_url': PROXY,
                      'urllib3_proxy_kwargs': {'username': USERNAME,
                                                'password': PASSWORD
                                               }
                      }
