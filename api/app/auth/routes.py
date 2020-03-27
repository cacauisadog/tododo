import json

from flask import request, jsonify

from flask_login import current_user
from app.auth import auth_svc, bp


@bp.route('/api/whoami', methods=['GET'])
def whoami():
    if current_user.is_authenticated:
        return jsonify(current_user.to_dict_json())

    return jsonify({'is_authenticated': False})


@bp.route('/api/signup', methods=['POST'])
def signup():
    user = json.loads(request.form.get('user'))
    new_user = auth_svc.signup(user)
    return jsonify(new_user)


@bp.route('/api/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify(current_user)

    user = json.loads(request.form.get('user'))
    user = auth_svc.login(user)
    return jsonify(user)


@bp.route('/api/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        auth_svc.logout()

    return jsonify({})
