import time
import jwt
from typing import Dict
from decouple import config

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')


def token_response(token: str):
    return {'access_token': token}


def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        'user_id': user_id,
        'expires': int(time.time()) * 3600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except jwt.ExpiredSignatureError:
        return 'Token expired.'
    except jwt.InvalidTokenError:
        return 'Invalid token.'
