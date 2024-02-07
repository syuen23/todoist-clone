from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf.csrf import generate_csrf

from api import db, login_manager
from ..forms.account import LoginForm, SignupForm
from ..models.account import Account


auth_bp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return Account.query.get(int(user_id))
    return None


@login_manager.unauthorized_handler
@auth_bp.route("/unauthorized", methods=["GET"])
def unauthorized():
    return {"error": "not authorized"}, 401


@auth_bp.route("/csrf", methods=["GET"])
def get_csrf():
    response = jsonify(detail="success")
    response.headers.set("X-CSRFToken", generate_csrf())
    return response


@auth_bp.route("/login", methods=["POST"])
def login():
    if not current_user.is_authenticated:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            account = db.session.scalar(
                db.select(Account).filter_by(email=email).limit(1),
            )
            if account and account.check_password(password):
                login_user(account)
            else:
                return {"error": "Incorrect credentials"}, 401

    return {"message": "Logged in successfully"}, 200


@login_required
@auth_bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return {"message": "Successfully logged out"}, 200


@auth_bp.route("/signup", methods=["POST"])
def signup():
    form = SignupForm(request.form)

    if not form.validate():
        return {"error": "Invalid form data"}, 400

    email = form.email.data
    password = form.password.data

    account = db.session.scalar(
        db.select(Account).filter_by(email=email).limit(1),
    )

    if account:
        return {"error": "Account already exists"}, 400

    account = Account(
        email=email,
    )
    account.set_password(password)

    db.session.add(account)
    db.session.commit()
    login_user(account)

    return {"message": "Account created successfully"}, 201
