from flask import request
from flask_restful import Resource
from models import db, User, UserSchema
from flask_bcrypt import Bcrypt
import random
import string

users_schema = UserSchema(many=True)
user_schema = UserSchema()
bcrypt = Bcrypt()


class Register(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, 400
        authKey = self.generate_key()
        json_data["authKey"] = authKey
        data = user_schema.load(json_data)
        # if errors:
        #     return errors, 422
        user = User.query.filter_by(username=data["username"]).first()
        email = User.query.filter_by(email=data["email"]).first()
        if user:
            return {"message": "User already exists"}, 400
        if email:
            return {"message": "Email already exists"}, 400
        password_hash = bcrypt.generate_password_hash(json_data["password"]).decode('utf-8')
        user = User(
            authKey=authKey,
            username=json_data["username"],
            email=json_data["email"],
            password=password_hash,
        )
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return {"token": result["authKey"]}, 201

    def generate_key(self):
        return "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(50)
        )


class Signin(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"error": "No input data provided"}, 400
        user = User.query.filter_by(email=json_data["email"]).first()
        if not user:
            return {"error": "User does not exist"}, 400
        if not bcrypt.check_password_hash(user.password, json_data["password"]):
            return {"error": "Email/Password incorrect"}, 400
        return {"token": user.authKey}, 200

class Authorize(Resource):
    def get(self):
        userToken = request.args.get('authKey')
        if not userToken:
            return {"error": "No input data provided"}, 400
        user = User.query.filter_by(authKey=userToken).first()
        if not user:
            return {"error": "User does not exist"}, 400
        user = user_schema.dump(user)
        return user, 200
