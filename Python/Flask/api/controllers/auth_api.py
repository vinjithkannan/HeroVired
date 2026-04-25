from flask_smorest import Blueprint, abort
from flask.views import MethodView
from extensions import db
from models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from schemas.user_schema import RegisterSchema, LoginSchema, UserResponseSchema

blp = Blueprint("auth", "auth", url_prefix="/api", description="Auth APIs")


# 🔹 REGISTER
@blp.route("/register")
class RegisterResource(MethodView):

    @blp.arguments(RegisterSchema)
    @blp.response(201)
    def post(self, data):
        if User.query.filter_by(username=data["username"]).first():
            return {"error": "Username already exists"}, 400

        user = User(name=data["name"], username=data["username"])
        user.set_password(data["password"])

        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully"}


# 🔹 LOGIN
@blp.route("/login")
class LoginResource(MethodView):

    @blp.arguments(LoginSchema)
    def post(self, data):
        user = User.query.filter_by(username=data["username"]).first()

        if not user or not user.check_password(data["password"]):
            return {"error": "Invalid credentials"}, 401

        token = create_access_token(identity=str(user.id))

        return {
            "message": "Login successful",
            "access_token": token
        }


# 🔹 PROFILE
@blp.route("/profile")
class ProfileResource(MethodView):

    @jwt_required()
    @blp.doc(security=[{"BearerAuth": []}])   # THIS IS KEY
    @blp.response(200, UserResponseSchema)
    def get(self):
        """
        Get current user profile
        ---
        security:
          - BearerAuth: []
        """
        user_id = int(get_jwt_identity())

        user = db.session.get(User, user_id)
        if not user:
            abort(404, message="User not found")

        return user