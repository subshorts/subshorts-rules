from flask import Blueprint

bp = Blueprint('', __name__, url_prefix='/')


@bp.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
