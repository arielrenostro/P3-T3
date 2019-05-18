from abc import ABC

from rest.dao.database import DAO


class Controller(ABC):

    _dao: DAO = None

    def __init__(self):
        for attr in ['_dao']:
            if not getattr(self, attr, None):
                raise AttributeError(f'Missing {attr} attribute')

    def find_all(self):
        return self._dao.find_all()

    def find(self, id_):
        return self._dao.find(id_)

    def update(self, entity):
        return self._dao.update(entity)

    def delete(self, entity):
        return self._dao.delete(entity)
