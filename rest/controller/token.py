from datetime import datetime, timedelta
from uuid import uuid4

from rest.controller.base import Controller
from rest.dao.token import TokenDAO
from rest.models.token import Token


class TokenController(Controller):

    _dao = TokenDAO()

    def find_by_token(self, token):
        return self._dao.find_by_token(token)

    def find_valid_by_token(self, token):
        entity = self._dao.find_by_token(token)
        if self.is_validate_token(entity):
            return token

    def find_or_generate_token(self, user):
        token = self._dao.find_by_user(user)
        if token and self.is_validate_token(token):
            return token.token

        return self._generate_token(user)

    def _generate_token(self, user):
        token = Token()

        token.token = str(uuid4())
        token.user = user
        token.user_id = user.id
        token.created_at = datetime.now()

        self._dao.update(token)

        return token.token

    @classmethod
    def is_validate_token(cls, token):
        if token:
            return (token.created_at + timedelta(hours=1)) > datetime.now()
