from flask import Flask

from flask_restful import Api,Resource,reqparse

from run import app

app.config['DEBUG'] =True

api = Api(app)

# my data structures to store users data as specified below
users = [{
                "username":"admin",
                "password":"admin"
         },
         {
                 "username":"attendant",
                 "password":"attendant"
         }
        ]


class User(Resource):
        
    def get(self,username):
        for user in users:
            if(username == user['username']):
                return user,200
                        
        return 'User not found ',404

    def post(self,username):
        parser = reqparse.RequestParser()
        parser.add_argument('password')
        args =parser.parse_args()

        for user in users:
            if(username == user['username']):
                return 'User with username {} already exists'.format(username),400

        user = {
                'username': username,
                'password': args['password']                
        }
        users.append(user)
        return user,201
    '''
    The post method is used to create a new user:
    '''
    def put(self,username):
        parser = reqparse.RequestParser()
        parser.add_argument('password')        
        args = parser.parse_args()

        for user in users:
            if(username == user['username']):
                user['password'] = args['password']                
                return user,200

        user = {
            'username':username,
            'password':args['password']            
        }

        users.append(user)
        return user,201

    def delete(self,username):
        global users
        users = [user for user in users if user['username'] != username]
        return "{} is deleted .".format(username), 200

api.add_resource(User,"/api/v1/user/<string:username>")

app.run(port=1995)
