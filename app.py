from flask import Flask

from core import register_core
from log import register_log
from database import register_db


def create_app():
    app = Flask(__name__, static_url_path='')
    app.config['SECRET_KEY'] = 'd76b9af7-0caf-4749-b671-65912beea187'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    register_log(app)
    register_db(app)
    register_core(app)

    return app
