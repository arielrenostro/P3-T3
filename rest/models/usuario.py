from _md5 import md5

from sqlalchemy import Column, String, Integer

from rest.database import Base


class Usuario(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    senha = Column(String(250))

    def __init__(self, email=None, senha=None):
        self.senha = senha
        self.email = email

    def __repr__(self):
        return f'{self.__class__.__name__} id [{self.id}] email [{self.email}]'

    def __setattr__(self, key, value):
        if key == 'senha':
            value = str(md5(value))
        super().__setattr__(key, value)
