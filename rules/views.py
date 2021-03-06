import urllib.parse

from flask import Blueprint, request, abort, redirect, render_template

from .models import PageRule

blueprint = Blueprint('', __name__, url_prefix='/')


@blueprint.route('/')
def index():
    return view(None)


@blueprint.route('/<path>')
def view(path):
    url = urllib.parse.urlparse(request.url)
    page_rules = PageRule.query.filter(PageRule.domain == url.netloc).all()
    if len(page_rules) > 0:
        page_rule: PageRule = page_rules[0]
        if page_rule.forwarding_domain:
            destination = f'{page_rule.forwarding_protocol}://{page_rule.forwarding_domain}'
            if page_rule.forwarding_path:
                destination += url.path
                if url.query != '':
                    destination += '?' + url.query
                if url.fragment != '':
                    destination += '#' + url.fragment
            return redirect(destination, code=page_rule.forwarding_code)
        elif page_rule.parking_title:
            return render_template('parking.html', page_rule=page_rule)
    abort(404)
