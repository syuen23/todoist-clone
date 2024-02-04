from flask import Blueprint, request
from api import db
from ..models.account import Account
from ..forms.account import SignupForm


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    return {"message": "Logged in successfully"}, 200


@auth_bp.route("/signup", methods=["POST"])
def signup():
    form = SignupForm(request.form)

    if not form.validate():
        return {"error": "Invalid form data"}, 400

    username = form.username.data
    email = form.email.data
    password = form.password.data

    account = db.session.execute(
        db.select(Account).filter_by(email=email),
    ).first()

    if account:
        return {"error": "Account already exists"}, 400

    account = Account(
        username=username,
        email=email,
    )
    account.set_password(password)

    db.session.add(account)
    db.session.commit()

    return {"message": "Account created successfully"}, 201


# from flask_wtf.csrf import generate_csrf

#     csrf_token = generate_csrf()
