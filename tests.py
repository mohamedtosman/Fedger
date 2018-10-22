from database import DbOperations
from flask import Flask, jsonify, request, make_response, abort
import app
import unittest
import datetime


db = DbOperations()

class TestEndpoints(unittest.TestCase):
	
	def testGetAllPets(self):
		"""Test get all pets (however, I am only testing the first pet only, the rest will follow the same format...you get the idea)"""
		pets = db.queryAllPets()
		self.assertEqual(pets[0]["id"], 1)
		self.assertEqual(pets[0]["name"], "Fritz")
		self.assertEqual(pets[0]["species"], "dog")
		self.assertEqual(pets[0]["gender"], "m")
		self.assertEqual(pets[0]["birthday"], datetime.date(2016, 12, 3))

	def testGetPet(self):
		"""Test successful case of quering a pet that already exsits using ID"""
		pet = db.getPetById("1")
		self.assertEqual(pet["id"], 1)
		self.assertEqual(pet["name"], "Fritz")
		self.assertEqual(pet["species"], "dog")
		self.assertEqual(pet["gender"], "m")
		self.assertEqual(pet["birthday"], datetime.date(2016, 12, 3))

	def testUpdatePet(self):
		"""Test updating first pet"""
		db.updatePet("2", "NotFritz", "Hamster", "w", "2018-10-21")
		pet = db.getPetById("2")
		self.assertEqual(pet["id"], 2)
		self.assertEqual(pet["name"], "NotFritz")
		self.assertEqual(pet["species"], "Hamster")
		self.assertEqual(pet["gender"], "w")
		self.assertEqual(pet["birthday"], datetime.date(2018, 10, 21))


if __name__ == '__main__':
    unittest.main()