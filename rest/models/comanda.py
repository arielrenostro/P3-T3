from sqlalchemy import Column, String, Numeric, Integer
from sqlalchemy.orm import relationship

from rest.database import Base


class Comanda(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    usuario = relationship("Usuario")
    produtos = Column(String(250))
    valor_total = Column(Numeric(2))

    def __init__(self, nome=None, email=None):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f'{self.__class__.__name__} id [{self.id}]'
