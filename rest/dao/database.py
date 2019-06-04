from abc import ABC

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session

db = SQLAlchemy()
#
# engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
# db_session = scoped_session(
#     session_factory=sessionmaker(
#         bind=engine,
#         expire_on_commit=False,
#         autocommit=False,
#         autoflush=False
#     )
# )
# Base = declarative_base()
# Base.query = db_session.query_property()

#
# def init_db():
#     import rest.models
#     Base.metadata.create_all(bind=engine)


class DAO(ABC):

    _entity_class = None

    def __init__(self):
        for attr in ['_entity_class']:
            if not getattr(self, attr, None):
                raise AttributeError(f'Missing {attr} attribute')

    def find_all(self):
        return self._entity_class.query.all()

    def find(self, id_):
        id_ = int(id_)
        return self._entity_class.query.get(id_)

    def update(self, entity):
        session: Session = db.session()

        session.add(entity)
        session.commit()

        return entity

    def delete(self, entity):
        session: Session = db.session()

        session.delete(entity)
        session.commit()
