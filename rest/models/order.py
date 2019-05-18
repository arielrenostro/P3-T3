from sqlalchemy import Column, String, Numeric, Integer, ForeignKey
from sqlalchemy.orm import relationship

from rest.dao.database import Base


class Order(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    products = Column(String(250))
    total_value = Column(Numeric(2))

    def __init__(self, user=None, products=None, total_value=None):
        self.user = user
        self.products = products
        self.total_value = total_value

    def __repr__(self):
        return f'{self.__class__.__name__} id [{self.id}]'
