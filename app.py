from flask import Flask, jsonify, request, make_response, abort
from flasgger import Swagger, swag_from
import pymysql.cursors
import json
import datetime
from database import DbOperations

app = Flask(__name__)
swagger = Swagger(app)
db = DbOperations()

class DatetimeEncoder(json.JSONEncoder):
	"""
	Used this class to bypass datetime parsing issue
	"""
	def default(self, obj):
		try:
			return super(DatetimeEncoder, obj).default(obj)
		except TypeError:
			return str(obj)

@app.route("/allPets", methods=["GET"])
@swag_from("allpets.yml")
def all_pets():
	"""
	Return all pets in database
	"""
	return json.dumps(db.queryAllPets(), cls=DatetimeEncoder)

@app.route("/getPet/<id>", methods=["GET"])
@swag_from("getpet.yml")
def get_pet(id):
	"""
	Return single pet from database using id
	"""
	return json.dumps(db.getPetById(id), cls=DatetimeEncoder)

@app.route("/updatePet/<id>", methods=["POST"])
@swag_from("updatepets.yml")
def update_pet(id):
	"""
	Update pet using id and return updated pet
	"""
	newName = request.args.get('name')
	newSpecies = request.args.get('species')
	newGender = request.args.get('gender')
	newBirthday = request.args.get('birthday')

	return json.dumps(db.updatePet(id, newName, newSpecies, newGender, newBirthday), cls=DatetimeEncoder)

if __name__ == "__main__":
	app.run()