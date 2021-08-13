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

class SpazioStatusRemoveResource(Resource):
	def delete(self, machine):
		toDelete = SpazioStatus.filter_by_machine(machine)
		for i in toDelete:
			i.delete()
		return 204

api.add_resource(SpazioStatusListResource, '/api/v1.0/spazioStatus/', endpoint='spazio_status_list_resource')
api.add_resource(SpazioStatusRemoveResource, '/api/v1.0/spazioStatus/machine/<machine>', endpoint='spazio_status_remove_resource')