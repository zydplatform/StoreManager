from flask import Flask,json,request, jsonify

app= Flask(__name__)

app.config['DEBUG'] =True

# my data structures to store particular data as specified below
users = []

class User:
    def __init__(self, name,access):
        self.name=name
        self.id = id
        self.password = password

@app.route('/api/v1/users/<string:name>', methods=['GET'])
def getUsers():
  return jsonify({'users':users})

@app.route('/api/v1/user/<int:user_id>', methods=['GET'])
def getUser(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user':user[0]})

@app.route('/api/v1/users/owner/<string:name>',methods=['POST'])  
def addUser():

    request_data = request.get_json()
    name = request_data.get('name')
    password = request_data.get('password') 

    if name == "" and password == "":
        return jsonify({"message":"Enter Username and Password"})

if __name__ == "__main__":
    app.run(port=5000)