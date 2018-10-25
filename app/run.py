import os
from flask import json,jsonify,app,Flask

app = Flask(__name__)

app.config['DEBUG'] =True

# @app.route('/',methods=['GET'])
# def index():
#     return jsonify({'App':'store manager'})


# if __name__ == '__main__':
#     app.run(port=5000)

