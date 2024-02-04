from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
)


class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=4, max=25),
        ],
    )
    email = EmailField(
        "Email",
        validators=[
            DataRequired(),
            Length(min=6),
            Email(message="Enter a valid email."),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(
                min=6,
                message="Select a stronger password",
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match.",
            ),
        ],
    )
