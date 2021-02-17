from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    authKey = db.Column(db.String(250), unique=True, nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )
    # tasks = db.relationship('Task', backref='user', lazy=True)

    def __init__(self, authKey, username, email, password):
        self.authKey = authKey
        self.username = username
        self.email = email
        self.password = password




class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    note = db.Column(db.String(250), unique=True, nullable=False)
    completed = db.Column(db.Boolean(), default=False, nullable=False)
    end_date = db.Column(db.TIMESTAMP, unique=True, nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )

    def __init__(self, title, note, end_date):
        self.title = authKey
        self.note = note
        self.end_date = end_date


class TaskSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    note = fields.String(required=True)
    completed = fields.Boolean(required=True)
    end_date = fields.DateTime(required=True)
    creation_date = fields.DateTime()



    
class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    authKey = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    creation_date = fields.DateTime()
    # tasks = fields.List(fields.Nested(TaskSchema))