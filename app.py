from flask import Flask
from flask_migrate import Migrate
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

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'

    return app


if __name__ == '__main__':
    create_app().run()
