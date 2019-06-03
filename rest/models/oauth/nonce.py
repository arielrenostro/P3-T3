from rest.dao.database import db


class Nonce(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer)
    nonce = db.Column(db.String(40))
    client_key = db.Column(db.String(40), db.ForeignKey('client.client_key'), nullable=False)
    client = db.relationship('Client')
    request_token = db.Column(db.String(50))
    access_token = db.Column(db.String(50))
