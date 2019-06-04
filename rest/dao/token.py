from rest.dao.database import DAO
from rest.models.token import Token


class TokenDAO(DAO):

    _entity_class = Token

    def find_by_user(self, user):
        query = self._entity_class.query

        return query.filter_by(
            user=user,
        ).first()

    def find_by_token(self, token):
        query = self._entity_class.query

        return query.filter_by(
            token=token,
        ).first()

    def delete_by_user(self, user):
        query = self._entity_class.query

        query.filter_by(
            user_id=user.id,
        ).delete()
