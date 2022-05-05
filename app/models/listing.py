from .db import db

class Listing(db.Model):

    __tablename__= 'listings'

    id = db.Column(db.Integer, primary_key= True)
    city = db.Column(db.String)
    address = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    price = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'address': self.address,
            'state': self.state,
            'country': self.country,
            'price': self.price
        }
