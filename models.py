from sqlalchemy import func

from app import db


class PageRule(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, onupdate=func.now(), server_default=func.now())

    domain = db.Column(db.String(255), unique=True)
    owner = db.Column(db.String(255), nullable=False)

    forwarding_protocol = db.Column(db.String(7), nullable=True)
    forwarding_domain = db.Column(db.String(255), nullable=True)
    forwarding_code = db.Column(db.SmallInteger, nullable=True)
    forwarding_path = db.Column(db.Boolean, nullable=True)

    parking_title = db.Column(db.String(63), nullable=True)
    parking_content = db.Column(db.Text(), nullable=True)
