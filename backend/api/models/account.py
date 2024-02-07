from api import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class Account(UserMixin, db.Model):
    __tablename__ = "account"

    id = db.Column(
        db.Integer,
        primary_key=True,
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
        return f"<User id={self.id}, email={self.email}>"
