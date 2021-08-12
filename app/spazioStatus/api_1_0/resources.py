from flask import Blueprint, request
from flask_restful import Api, Resource
from .schemas import SpazioStatusSchema
from ..models import SpazioStatus

spazio_status_bp = Blueprint('spazio_status_bp', __name__)

spazioStatusSchema = SpazioStatusSchema()

api = Api(spazio_status_bp)

class SpazioStatusListResource(Resource):
	def get(self):
		spazioStatus = SpazioStatus.get_all()
		result = spazioStatusSchema.dump(spazioStatus, many=True)
		return result

api.add_resource(SpazioStatusListResource, '/api/v1.0/spazioStatus/', endpoint='spazio_status_list_resource')