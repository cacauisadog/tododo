from sqlalchemy.orm import backref

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.utcnow)
    todo_lists = db.relationship('TodoList', backref=backref('creator', cascade="delete"), lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict_json(self):
        d = {
            'id': self.id,
            'is_active': self.is_active,
            'username': self.username,
            'email': self.email,
            'is_authenticated': self.is_authenticated
        }
        return d

    def __repr__(self):
        return '<User {} ({})>'.format(self.username, self.email)


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(64), index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, index=True, nullable=True, onupdate=datetime.utcnow)
    todos = db.relationship('Todo', backref=backref('list', cascade="delete"), lazy='dynamic')

    def to_dict_json(self):
        d = {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'todos': [todo.to_dict_json() for todo in self.todos]
        }
        return d

    def __repr__(self):
        return '<TodoList {} {}>'.format(self.title, self.creator)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
    text = db.Column(db.Text)
    is_done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, nullable=True, onupdate=datetime.utcnow)

    def to_dict_json(self):
        d = {
            'id': self.id,
            'text': self.text,
            'is_done': self.is_done,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        return d

    def __repr__(self):
        return '<Todo {} {}}>'.format(self.text, self.list)
