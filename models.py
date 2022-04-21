from sqlalchemy import func

from app import db


class PageRule(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, onupdate=func.now(), server_default=func.now())

    domain = db.Column(db.String(255), unique=True)
    owner = db.Column(db.String(255), nullable=False, index=True)

    forwarding_protocol = db.Column(db.String(7), nullable=True)
    forwarding_domain = db.Column(db.String(255), nullable=True)
    forwarding_code = db.Column(db.SmallInteger, nullable=True)
    forwarding_path = db.Column(db.Boolean, nullable=True)

    parking_title = db.Column(db.String(63), nullable=True)
    parking_content = db.Column(db.Text(), nullable=True)

    @staticmethod
    def serialize(obj) -> dict:
        return {
            'id': obj.id,
            'created_at': str(obj.created_at),
            'updated_at': str(obj.updated_at),
            'domain': obj.domain,
            'owner': obj.owner,
            'forwarding_protocol': obj.forwarding_protocol,
            'forwarding_domain': obj.forwarding_domain,
            'forwarding_code': obj.forwarding_code,
            'forwarding_path': obj.forwarding_path,
            'parking_title': obj.parking_title,
            'parking_content': obj.parking_content,
        }

    @staticmethod
    def deserialize(json: dict):
        obj = PageRule()
        obj.id = json.get('id')
        obj.created_at = json.get('created_at')
        obj.updated_at = json.get('updated_at')
        obj.domain = json.get('domain')
        obj.owner = json.get('owner')
        obj.forwarding_protocol = json.get('forwarding_protocol')
        obj.forwarding_domain = json.get('forwarding_domain')
        obj.forwarding_code = json.get('forwarding_code')
        obj.forwarding_path = json.get('forwarding_path')
        obj.parking_title = json.get('parking_title')
        obj.parking_content = json.get('parking_content')
        return obj
