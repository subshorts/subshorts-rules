from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    import models

    import views
    app.register_blueprint(views.bp)

    api = Api(app)
    import apis
    api.add_namespace(apis.page_rules, '/api/rules')

    return app


if __name__ == '__main__':
    create_app().run()
