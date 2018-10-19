# Kiganda Ivan StoreManager Api
This is a functional web application for managing a single store.

 
![Coveralls github](https://img.shields.io/coveralls/github/jekyll/jekyll.svg)

[![Build Status](https://travis-ci.org/zydplatform/StoreManager.svg?branch=master)]
(https://travis-ci.org/zydplatform/StoreManager)

 
![Libraries.io for GitHub](https://img.shields.io/librariesio/github/phoenixframework/phoenix.svg)

 
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)


API endpoints to manage store data

Maintainability

Build Status

Coverage Status

$pytest
Versioning
This is version one"v1" of the API
End Points(Required Features)
End Point	Functionality
GET api/v1/products/int:productId	Fetch a product
POST api/v1/attendant/sales	Add a sale order
GET api/v1/sales/int:saleId	Fetch a specific sale order
GET api/v1/admin/sales	Admin fetch all sale orders
POST api/v1/admin/products	Create a product
GET api/v1/products	Fetch all products


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

$python app.py
Test app in terminal

