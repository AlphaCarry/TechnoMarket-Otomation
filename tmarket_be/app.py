from flask import Flask
from flask_migrate import Migrate

from blueprints import api_bp
from dp import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://tmarket_user:Alpha@localhost/tmarket_db"
    migrate = Migrate()

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return {'sunucu': 'ok'}
# sıkıntılı bir yer
    app.register_blueprint(api_bp, url_prefix='/api')
    return app

