'''
Created on Sep 28, 2017

@author: bhatsubh
'''
import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.users import UserRegister
from resources.items import Item  
from resources.items import ItemList
from resources.store import StoreList,Store

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'random'
api = Api(app)

jwt = JWT(app,authenticate,identity) #/auth

     
api.add_resource(Item,'/Item/<string:name>')
api.add_resource(ItemList,'/Items')
api.add_resource(StoreList,'/Stores')
api.add_resource(Store,'/Store/<string:name>')
api.add_resource(UserRegister,'/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
