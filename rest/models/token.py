from rest.dao.database import db


class Token(db.Model):

    __tablename__ = 'token'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User")
    token = db.Column(db.String)
    created_at = db.Column(db.DateTime)

    def __init__(self, user=None, token=None, created_at=None):
        self.user = user
        self.token = token
        self.created_at = created_at

    def __repr__(self):
        return f'{self.__class__.__name__} id [{self.id}] user [{self.user}] token [{self.token}]'
