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

    import rules.views
    app.register_blueprint(rules.views.bp)

    api = Api(app)
    import apis.views
    api.add_namespace(apis.views.page_rules, '/api/rules')

    return app


if __name__ == '__main__':
    create_app().run()
