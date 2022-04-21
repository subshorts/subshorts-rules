from flask import request
from flask_restx import Namespace, Resource, abort

from app import db
from models import PageRule

page_rules = Namespace('Page Rules')


@page_rules.route('')
class PageRuleView(Resource):
    def get(self):
        queryset = PageRule.query.all()
        return list(map(PageRule.serialize, queryset))

    def post(self):
        obj = PageRule.deserialize(request.json)
        db.session.add(obj)
        db.session.commit()
        return PageRule.serialize(obj)


@page_rules.route('/<int:id>')
class PageRuleDetailView(Resource):
    def get(self, id):
        obj = self.get_object(id)
        return PageRule.serialize(obj)

    def put(self, id):
        return 'update'

    def delete(self, id):
        return 'delete'

    def get_object(self, id):
        obj = PageRule.query.get(id)
        if obj is None:
            abort(404)
        return obj
