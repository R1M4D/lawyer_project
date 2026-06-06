from datetime import datetime
from sqlalchemy.orm import backref
from extension import db
from flask_login import UserMixin

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))

    service_type = db.Column(db.String(255))
    situation = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
