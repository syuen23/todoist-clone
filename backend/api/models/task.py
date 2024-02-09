from api import db
from enum import Enum


class PriorityLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Task(db.Model):
    __tablename__ = "task"

    task_id = db.Column(
        db.Integer,
        primary_key=True,
    )

    project_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "project.project_id",
        ),
    )

    title = db.Column(
        db.String(255),
        nullable=False,
    )

    description = db.Column(
        db.Text,
    )

    due_date = db.Column(
        db.Date,
    )

    priority = db.Column(
        db.Enum(PriorityLevel),
        default=PriorityLevel.LOW,
    )
