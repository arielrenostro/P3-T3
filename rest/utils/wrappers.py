from functools import wraps

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
            body = {
                'fail': {
                    'text': str(e)
                }
            }
            return body, 500

    return wrapper
