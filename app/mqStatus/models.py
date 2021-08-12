from app.db import db, BaseModelMixin

class MQStatus(db.Model, BaseModelMixin):
	__tablename__ = 'MQStatus'

	id = db.Column(db.Integer, primary_key=True)
	machine = db.Column(db.String, nullable=False)
	qm = db.Column(db.String, nullable=False)
	status = db.Column(db.String, nullable=False)
	dangerLevel = db.Column(db.String, nullable=False)
	problemGroup = db.Column(db.String, nullable=False)
	date = db.Column(db.String, nullable=False)