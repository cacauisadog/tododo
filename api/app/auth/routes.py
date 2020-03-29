import json

from flask import request, jsonify

from flask_login import current_user
from app.auth import auth_svc, bp


"""
    As of flask v1.1, the `return` statement will automatically `jsonify` a dictionary in the first return value. So you 
    can simply use `return dict, 200`. Note that 200 is the default status_code.
    https://stackoverflow.com/questions/45412228/flask-sending-data-and-status-code-through-a-response-object
"""
@bp.route('/api/whoami', methods=['GET'])
def whoami():
    if current_user.is_authenticated:
        return current_user.to_dict_json()

    return {'is_authenticated': False}


@bp.route('/api/signup', methods=['POST'])
def signup():
    user = json.loads(request.form.get('user'))
    new_user = auth_svc.signup(user)
    return new_user


@bp.route('/api/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return current_user

    user = json.loads(request.form.get('user'))
    user = auth_svc.login(user)
    return user


@bp.route('/api/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        auth_svc.logout()

    return {}
