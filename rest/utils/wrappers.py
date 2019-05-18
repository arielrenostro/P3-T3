import traceback
from functools import wraps

from sqlalchemy.exc import IntegrityError

from rest.exceptions.request import RequestException


def authenticated(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper


def exception_handler(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except RequestException as e:
            return e.body, e.http_status
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
