from api import db
from account import Account


class Project(db.Model):
    __tablename__ = "project"

    project_id = db.Column(
        db.Integer,
        primary_key=True,
    )

    account_id = db.Column(
        db.Integer,
        db.ForeignKey("Account.id"),
    )

    name = db.Column(
        db.String(200),
        unique=True,
        nullable=False,
    )

    description = db.Column(
        db.Text,
    )

    tasks = db.relationship(
        "task",
        back_populate="project",
        lazy=True,
    )
