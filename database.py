import pymysql.cursors
import json
import datetime

connection = pymysql.connect(host='localhost',
							 user='FILL IN YOUR USERNAME HERE',
							 password='FILL IN YOUR PASSWORD HERE',
							 db='petdb',
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)

class DbOperations:
	def queryAllPets(self):
		"""
		Get all pets available in the database
		"""
		with connection.cursor() as cursor:
			sql = "SELECT * FROM pets"
			cursor.execute(sql)
			pets = cursor.fetchall()
			return pets

	def getPetById(self, id):
		"""
		Check if pet exists using id
		"""
		if(not self.checkIdFormat(id)):
			abort(403, description="Id must be an integer!")
		with connection.cursor() as cursor:
			sql = "SELECT * FROM pets WHERE id = '" + str(id) + "'"
			cursor.execute(sql)
			pet = cursor.fetchone()
			if pet:
				return pet
			abort(404, description="Pet does not exist in database!")

	def updatePet(self, id, newName, newSpecies, newGender, newBirthday):
		"""
		Check if pet exists in database, it if is, update it and then return the new value
		"""
		pet = self.getPetById(id)
		if(pet):
			if(not self.checkEnteredValues(newGender, newBirthday)):
				abort(403, description="One or more input is wrong. Please check proper format!")
			with connection.cursor() as cursor:
				cursor.execute("UPDATE pets SET name=%s, species=%s, gender=%s, birthday =%s WHERE id=%s",
					(newName, newSpecies, newGender, newBirthday, id))
				connection.commit()
				return self.getPetById(id)
		abort(404, description="Failed to update since pet does not exist in database!")

	def checkIdFormat(self, id):
		"""
		Check if id is an integer
		"""
		if id.isdigit():
			return True
		return False

	def checkEnteredValues(self, newGender, newBirthday):
		"""
		Check that gender is either 'w' or 'm' and birthday is in a proper YY-MM-DD format
		"""
		if newGender != "w" and newGender != "m":
			return False
		elif newBirthday:
			try:
				datetime.datetime.strptime(newBirthday, '%Y-%m-%d')
				return True
			except ValueError:
				return False
		else:
			return True
