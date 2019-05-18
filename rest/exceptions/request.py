class RequestException(Exception):

    http_status = None
    body = None

    def __init__(self, http_status=500, message=None, body={}):
        super().__init__()

        if not body:
            body = {}

        if message:
            body.update({
                'fail': {
                    'text': message
                }
            })

        self.http_status = http_status
        self.body = body
