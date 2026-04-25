from flask import Flask
from config import Config
from extensions import db, jwt
from controllers.auth_api import blp as auth_blp
from flask_smorest import Api

app = Flask(__name__)
app.config.from_object(Config)

# OpenAPI 3 config
app.config["API_TITLE"] = "Auth API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["OPENAPI_JSON_PATH"] = "openapi.json"

# THIS IS IMPORTANT (global security)
app.config["OPENAPI_SECURITY"] = [{"BearerAuth": []}]

db.init_app(app)
jwt.init_app(app)

api = Api(app)
# manually inject security scheme into spec
api.spec.components.security_scheme(
    "BearerAuth",
    {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    }
)
api.register_blueprint(auth_blp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)