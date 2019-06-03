from rest.dao.database import DAO
from rest.models.user import User


class UserDAO(DAO):

    _entity_class = User

    def find_by_email_password(self, email, password):
        query = self._entity_class.query

        return query.filter_by(
            email=email,
            password=password
        ).first()
