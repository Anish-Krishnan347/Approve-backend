from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    # Database configuration
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="novaglow--+",
    hostname="localhost",
    databasename="APPROVE",
    )


    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Register blueprints
    from app.routes.role_routes import role_bp
    app.register_blueprint(role_bp, url_prefix="/api/role")

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/api/user")

    from app.routes.approve_routes import approve_bp
    app.register_blueprint(approve_bp, url_prefix="/api/approve")

    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    from app.routes.permission_routes import permission_bp
    app.register_blueprint(permission_bp, url_prefix="/api/permission")

    # Create tables
    with app.app_context():
        db.create_all()

    return app
