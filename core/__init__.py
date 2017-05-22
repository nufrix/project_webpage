# -*- encoding: utf-8 -*-
from flask import Blueprint

from .views import index


def register_core(app):
    user_blueprint = Blueprint('',
                               __name__,
                               template_folder='templates',
                               url_prefix='/')
    user_blueprint.add_url_rule('/',
                                view_func=index,
                                endpoint='index')
    app.register_blueprint(user_blueprint)
