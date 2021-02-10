from flask import Blueprint
from flask_restful import Api
from resources.health import Health
from resources.user import UserResource
from resources.authenticate import Register, Signin, Authorize

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Route
api.add_resource(Health, "/health")
api.add_resource(UserResource, "/user")
api.add_resource(Register, "/register")
api.add_resource(Signin, "/signin")
api.add_resource(Authorize, "/authorize")
