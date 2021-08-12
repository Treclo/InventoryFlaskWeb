from flask import Blueprint, request
from flask_restful import Api, Resource
from .schemas import TXStatusSchema
from ..models import TXStatus

tx_status_bp = Blueprint('tx_status_bp', __name__)

txStatusSchema = TXStatusSchema()

api = Api(tx_status_bp)

class TXStatusListResource(Resource):
	def get(self):
		spazioStatus = TXStatus.get_all()
		result = txStatusSchema.dump(spazioStatus, many=True)
		return result

api.add_resource(TXStatusListResource, '/api/v1.0/txStatus/', endpoint='tx_status_list_resource')