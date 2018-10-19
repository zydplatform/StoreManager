from flask import Flask,jsonify

app = Flask(__name__)

app.debug=True

@app.route('/api/v1')
def home():
    return jsonify({"home_page":"welcome home"})

if __name__ == "__main__":
    app.run(port=5000)

