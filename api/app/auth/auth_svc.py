from app import db
from app.models import User
from flask_login import login_user, logout_user


def signup(user_dic):
    username, email, password = user_dic['username'], user_dic['email'], user_dic['password']
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return {'error': 'Email already in use!'}

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    user = new_user.to_dict_json()
    return user


def login(user_dic):
    email, password = user_dic['email'], user_dic['password']
    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        return {'error': 'Invalid email or password!'}

    login_user(user)
    return user.to_dict_json()


def logout():
    logout_user()
