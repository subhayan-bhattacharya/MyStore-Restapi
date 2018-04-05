'''
Created on Sep 28, 2017

@author: bhatsubh
'''
import sqlite3
from flask_restful import Resource,reqparse
from models.user_model import UserModel

   
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="This field cannot be blank,should have the user name"
    )
    parser.add_argument('password',
            type=str,
            required=True,
            help="This is the password,should not be left blank"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        
        user = UserModel.find_by_username(data['username'])
        if user:
            return {"message" : "a user with that user name already exists"},400
        else:
            user = UserModel(data['username'],data['password'])
            user.save_to_db()
            return {"message" : "User created successfully"},201
        