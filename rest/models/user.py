import hashlib

from sqlalchemy import Column, String, Integer

from rest.dao.database import Base


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True)
    password = Column(String(250))

    def __init__(self, email=None, password=None):
        self.password = password
        self.email = email

    def __repr__(self):
        return f'{self.__class__.__name__} id [{self.id}] email [{self.email}]'

    def __setattr__(self, key, value):
        if key == 'password':
            m = hashlib.sha512()
            m.update(str(value).encode("utf-8"))
            value = str(m.hexdigest())
        super().__setattr__(key, value)
