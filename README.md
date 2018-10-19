# Kiganda Ivan StoreManager Api
This is a functional web application for managing a single store.

 Coverage Status
![Coveralls github](https://img.shields.io/coveralls/github/jekyll/jekyll.svg)

Travis ci Build Status
![Build Status](https://travis-ci.org/zydplatform/StoreManager.svg?branch=master)
(https://travis-ci.org/zydplatform/StoreManager)

 
 
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)


$pytest
Versioning
This is version one"v1" of the API
End Points(Required Features)
End Point	Functionality
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
***




Create virtual environment and activate it

$pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
Install all the necessary tools by

$pip insatll -r requirements.txt
Start app server in console/terminal/commandprompt
