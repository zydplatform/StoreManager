from flask import Flask,jsonify,json

app = Flask(__name__)

app.config['DEBUG'] =True

@app.route('/')
def index():
    return jsonify({'App':'store manager'})

if __name__ == "__main__":
    app.run(port=5000)