from rest.dao.database import DAO
from rest.dao.token import TokenDAO
from rest.models.user import User


class UserDAO(DAO):

    _entity_class = User

    def find_by_email_password(self, email, password):
        query = self._entity_class.query

        return query.filter_by(
            email=email,
            password=password
        ).first()

    def delete(self, entity):
        _token_dao = TokenDAO()
        _token_dao.delete_by_user(entity)

        super().delete(entity)
