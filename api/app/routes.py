import json

from flask import request, jsonify

from app import api
from flask_login import current_user
from app.services import auth_svc


@api.route('/api/whoami', methods=['GET'])
def whoami():
    if current_user.is_authenticated:
        return jsonify(current_user.to_dict_json())

    return jsonify({'is_authenticated': False})


@api.route('/api/signup', methods=['POST'])
def signup():
    user = json.loads(request.form.get('user'))
    new_user = auth_svc.signup(user)
    return jsonify(new_user)


@api.route('/api/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify(current_user)

    user = json.loads(request.form.get('user'))
    user = auth_svc.login(user)
    return jsonify(user)


@api.route('/api/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        auth_svc.logout()

    return jsonify({})
