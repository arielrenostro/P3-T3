import traceback
from functools import wraps
from http import HTTPStatus
from http.cookies import SimpleCookie

from flask import request
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import Unauthorized

from rest.exceptions.request import RequestException


def authenticated(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = None

        cookie_header = request.headers.get('Cookie')
        if cookie_header:
            cookie = SimpleCookie(input=cookie_header)
            if 'X-Furb-Authorization' in cookie:
                token = cookie['X-Furb-Authorization'].value

        if not token:
            token = request.headers.get('X-Furb-Authorization')

        from rest.controller.token import TokenController
        if TokenController().find_valid_by_token(token):
            return fn(*args, **kwargs)

        return '', HTTPStatus.FORBIDDEN
    return wrapper


def exception_handler(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except RequestException as e:
            return e.body, e.http_status
        except Unauthorized as e:
            body = {
                'fail': {
                    'text': e.description
                }
            }
            return body, e.code
        except Exception as e:
            if isinstance(e, IntegrityError):
                if 'UNIQUE' in str(e):
                    s = str(e).split('\n')[0].split(' ')
                    last = s[len(s) - 1]

                    body = {
                        'fail': {
                            'text': f'Conflict {last}'
                        }
                    }
                    return body, 409

            body = {
                'fail': {
                    'text': str(e),
                    'stacktrace': traceback.format_exc()
                }
            }
            print(traceback.format_exc())
            return body, 500

    return wrapper
