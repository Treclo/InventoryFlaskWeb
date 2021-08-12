from flask import Blueprint, request
from flask_restful import Api, Resource
from .schemas import MQStatusSchema
from ..models import MQStatus

mq_status_bp = Blueprint('mq_status_bp', __name__)

mqStatusSchema = MQStatusSchema()

api = Api(mq_status_bp)

class MQStatusListResource(Resource):
	def get(self):
		spazioStatus = MQStatus.get_all()
		result = mqStatusSchema.dump(spazioStatus, many=True)
		return result

api.add_resource(MQStatusListResource, '/api/v1.0/mqStatus/', endpoint='mq_status_list_resource')