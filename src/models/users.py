from . import db
# from ._enums import Roles
from passlib.hash import pbkdf2_sha256 as sha256
from src.errors import NotFoundError
################################################################################

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '{}<{}>'.format(self.username, self.id)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def get(cls, id=None, limit=1000, offset=0):
        query = cls.query
        if id is not None:
            query = query.filter_by(id=id)
            if not query.first():
                raise NotFoundError('ID {} does not exist.'.format(id))
        query = query.limit(limit)
        query = query.offset(offset)

        return [i.serialize for i in query.all()]

    @classmethod
    def create(cls):
        return []

    @classmethod
    def update(cls):
        return []

    @classmethod
    def delete(cls):
        return []

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
