from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    todo_lists = db.relationship('TodoList', backref='creator', lazy='dynamic')

    def __repr__(self):
        return '<User {} ({})>'.format(self.username, self.email)


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(64), index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    todos = db.relationship('Todo', backref='list', lazy='dynamic')

    def __repr__(self):
        return '<TodoList {} {}>'.format(self.title, self.creator)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
    text = db.Column(db.Text)
    is_done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def __repr__(self):
        return '<Todo {} {}}>'.format(self.text, self.list)
