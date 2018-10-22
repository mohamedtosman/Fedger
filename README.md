## Task:
Specify, implement and test a RESTful HTTP-Web-Service to list and update pet information.

## Prerequisites:
MySQL
Python3.x

## Installation:
```
python -m pip install PyMySQL
pip install flask
pip install flasgger
```

## Files:
**app.py**
	Contains app initialization using flask and endpoints/routes that call database functions upon execution

**database.py**
	Contains database manipulation methods that get used in app.py

**.yml files**
	Contains specification for each endpoint by using the @swag_from decorator

## Usage:
***Enter username and password for MySQL account at line 6 and 7 in database.py to connect to the database***

* Execute the following command to load sql dump into MySQL. Replace "username" by your MySQL username and you will then be prompted to enter your password:

`mysql -u username -p petdb < SQLModel.sql`

* Run the application:

`python app.py`

Navigate to following URL to view the Swagger API and try out the endpoint using the 'Try it out' option:

`http://localhost:5000/apidocs/`


## Testing:
`python tests.py`

## API Documentation:
**GET: /allPets**

Retrieve all pets from database

**POST: /getPet/<id>**

Retrieve single pet using passed in ID

```
Parameters:
	id - string
```

**POST: /updatePet/<id>**

Update specific pet if found in database using ID

```
Parameters:
	id - string
	name - string
	species - string
	gender - string
	birthday - string
```
