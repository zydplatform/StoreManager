Kiganda Ivan StoreManager-API

 coveralls
![Coveralls github](https://img.shields.io/coveralls/github/jekyll/jekyll.svg)

 License
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)

Building Passing Tests
 
![Travis (.org)](https://img.shields.io/travis/:user/:repo.svg)





API endpoints to manage store data

Maintainability

Build Status

Coverage Status
GET api/v1/products/int:product_id	get a product
POST api/v1/attendant/sales	Add a sale order
GET api/v1/sales/int:sale_id	get a specific sale order
GET api/v1/owner/sales	Owner fetch all sale orders
POST api/v1/owner/products	Create a product
GET api/v1/products	get all products


Tools
Text editor where we write our project files. (VScode)
Flask Python Framework -Server-side framework
Pytest - a Python Testing Framework
Pylint - a Python linting library
Postman -Application to test and consume endpoints
PEP8 - Style guide
Getting Started clone the github repo to your computer:
https://github.com/zydplatform/StoreManager/tree/develop


Extract the zip file to another file
Create virtual environment and activate it

$pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
Install all the necessary tools by

$pip install -r requirements.txt
Start app server in console/terminal/commandprompt

$python app.py
Test app in terminal

$pytest
Versioning
This is first version "v1" of the Store Manager API

