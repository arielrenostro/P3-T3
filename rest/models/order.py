from rest.dao.database import db


class Order(db.Model):

    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User")
    products = db.Column(db.String(250))
    total_value = db.Column(db.Numeric(2))

    def __init__(self, user=None, products=None, total_value=None):
        self.user = user
        self.products = products
        self.total_value = total_value

    def __repr__(self):
        return f'{self.__class__.__name__} id [{self.id}]'
