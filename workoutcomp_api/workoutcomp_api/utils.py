from django.contrib.auth import authenticate
from common.utils import get_env_var
import json
import jwt
import requests

def jwt_get_username_from_payload_handler(payload):
    print(payload)
    username = payload.get('sub').replace('auth0|', '')
    authenticate(remote_user=username)
    return username

def jwt_decode_token(token):
    
    AUTH0_DOMAIN = get_env_var('AUTH0_DOMAIN')
    AUTH0_AUDIENCE = get_env_var('AUTH0_AUDIENCE')

    header = jwt.get_unverified_header(token)
    jwks = requests.get('{}/.well-known/jwks.json'.format(AUTH0_DOMAIN)).json()
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = '{}/'.format(AUTH0_DOMAIN)
    return jwt.decode(token, public_key, audience=AUTH0_AUDIENCE, issuer=issuer, algorithms=['RS256'])