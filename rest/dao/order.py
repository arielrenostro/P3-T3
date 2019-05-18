from rest.dao.database import DAO
from rest.models.order import Order


class OrderDAO(DAO):

    _entity_class = Order
