from api import db
from werkzeug.security import generate_password_hash, check_password_hash


class Account(db.Model):
    __tablename__ = "account"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    username = db.Column(
        db.String(100),
        nullable=False,
        unique=False,
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False,
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False,
    )

    def set_password(self, password):
        self.password = generate_password_hash(
            password,
            method="pbkdf2",
        )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.username)
