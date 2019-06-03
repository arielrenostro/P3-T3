from rest.dao.database import db


class AccessToken(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    client_key = db.Column(db.String(40), db.ForeignKey('client.client_key'), nullable=False)
    client = db.relationship('Client')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    token = db.Column(db.String(255))
    secret = db.Column(db.String(255))

    _realms = db.Column(db.Text)

    @property
    def realms(self):
        if self._realms:
            return self._realms.split()
        return []
