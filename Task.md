# Task Description

Specify, implement and test a RESTful HTTP-Web-Service to list and update pet information. In detail your tasks are:

* Write a RESTful HTTP-Web-API specification in [Swagger](http://swagger.io/specification/)
  * API requests and responses shall be in JSON
* Store the pet data in a MySQL database
  * `SQLModel.sql` contains the schema definition and initial dump of data
* Provide an RESTful HTTP-Web-Service Service with:
  * An endpoint to list all stored pets
  * An endpoint to update one pet by its id
  * Implement those endpoints in Python 3
* Write unit / integration tests for your endpoints
* Provide a README file with usage / run instructions and a short description of your work

## Hints

* You may use the builtin MySQL tools to import the dump
* Use any pure Python frameworks and libraries you like
* Use good and established coding standards and naming
* You may use [`PyMySQL`](https://github.com/PyMySQL/PyMySQL) to connect to MySQL
* Even if your implementation is not 100% working, please hand in your results anyway
* Send questions regarding the task to thomas@fedger.io
