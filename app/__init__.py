from flask import  Flask

app = Flask(__name__)

from app.products import Product
from app.sales import Sale
from app.users import User
from app.products import Allproducts
from app.sales import Allsales
from app.users import Allusers

# from flask_api import FlaskAPI

# from app.config import app_config

# def create_app(config_name):
#     app = FlaskAPI(__name__,instance_relative_config=True)
#     # app.config.from_object(app_config[config_name])
#     app.config.from_pyfile('config.py')

#     return app

