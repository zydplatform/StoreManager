from flask import Flask,app
from config import app_configuration

app = Flask(__name__)

app.config['DEBUG'] = True
@app.route('/')
def index():
    return 'my store manager'
if __name__=='__main__':
    app.run(port=5000)