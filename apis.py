from flask_restx import Namespace, Resource

page_rules = Namespace('Page Rules')


@page_rules.route('')
class PageRuleView(Resource):
    def get(self):
        return 'list'

    def post(self):
        return 'create'


@page_rules.route('/<int:id>')
class PageRuleDetailView(Resource):
    def get(self, id):
        return 'retrieve'

    def put(self, id):
        return 'update'

    def delete(self, id):
        return 'delete'
