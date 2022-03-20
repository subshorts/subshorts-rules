import urllib.parse

from flask import Blueprint, request, abort

from models import PageRule

bp = Blueprint('', __name__, url_prefix='/')


@bp.route('/')
def index():
    return view(None)


@bp.route('/<path>')
def view(path):
    url = urllib.parse.urlparse(request.url)
    page_rules = PageRule.query.filter(PageRule.domain == url.netloc).all()
    if len(page_rules) > 0:
        page_rule: PageRule = page_rules[0]
        if page_rule.forwarding_domain:
            return 'forwarding'
        elif page_rule.parking_title:
            return 'parking'
    abort(404)
