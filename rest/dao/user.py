from rest.dao.database import DAO
from rest.models.user import User


class UserDAO(DAO):

    _entity_class = User
