from flask import Blueprint
from flask_restful import Api, Resource
from .schemas import SpzWebSchema
from ..models import SpzWeb

spzweb_bp = Blueprint('spzweb_bp', __name__)

spzWebSchema = SpzWebSchema()

api = Api(spzweb_bp)

class SpzWebListResource(Resource):
	def get(self):
		list = SpzWeb.get_all()
		result = spzWebSchema.dump(list, many=True)
		return result

class SpzWebListResourceById(Resource):
	def put(self, id):
		user = SpzWeb.get_by_id(id)
		user.updateDate()
		return 200

api.add_resource(SpzWebListResource, '/api/v1.0/spz_web/', endpoint='spz_web_list_resource')
api.add_resource(SpzWebListResourceById, '/api/v1.0/spz_web/<id>', endpoint='spz_web_list_resource_by_id')