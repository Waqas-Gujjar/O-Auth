from django.conf import settings
from urllib.parse import urljoin , urlencode
from django.core.cache import cache
from googler import security

GOOGLE_AUTH_CACHE_KEY_PREFIX = 'google:auth:state'

GOOGLE_CLIENT_ID = settings.GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET  = settings.GOOGLE_CLIENT_SECRET 



def get_google_auth_callback_url(drop_http=False,force_https=False):
    url = urljoin(settings.BASE_URL, settings.GOOGLE_AUTH_CALLBACK_PATH)

    if drop_http:
        url = url.replace('http://', 'https://')

    if force_https:
        url = url.replace('http://', 'https://')
    
    return url

def generate_auth_url():
    redirect_uri = get_google_auth_callback_url()

    google_auth_client_id = GOOGLE_CLIENT_ID

    scope =" ".join(
        ['openid', 'email', 'profile']
        )

    state = security.generate_state()

    code_verifier, code_challenge = security.generate_pkce_pair()

    cache_key = f"{GOOGLE_AUTH_CACHE_KEY_PREFIX}:{state}"
    cache.set(cache_key, code_verifier, 300)
    
    params = {
        'client_id': google_auth_client_id,
        'redirect_uri': redirect_uri ,
        'response_type': 'code',
        'scope': scope,
        'state': state ,
        'code_challenge': code_challenge,
        'code_challenge_method': 'S256',
        'access_type': 'offline',

    }
    encoded_params = urlencode(params)
    google_auth_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    return urljoin(google_auth_url, f"?{encoded_params}")


def verify_google_auth_callback(state):
    cache_key = f"{GOOGLE_AUTH_CACHE_KEY_PREFIX}:{state}"
    code_verifier = cache.get(cache_key)
    pass





