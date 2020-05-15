from flask_login import UserMixin
from blog.database import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True, nullable=True, unique=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_id(self):
        return self.email

def load_user(email):
    return db.session.query(User).filter(User.email == email).first()
