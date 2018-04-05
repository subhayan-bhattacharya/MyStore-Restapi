'''
Created on Sep 29, 2017

@author: bhatsubh
'''
from flask_restful import Resource
from models.store_model import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return {"stores": store.json() }
        else:
            return {"message" : 'Store not found'},404
        
    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return {"message" : "Store '{}' already exists".format(name)},400
        else:
            new_store = StoreModel(name)
            new_store.save_to_db()
            return new_store.json(),201
    
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message" : "Store '{}' deleted".format(name)}
    
class StoreList(Resource):
    def get(self):
        stores = []
        for store in StoreModel.query.all():
            stores.append(store.json())
        return {"stores" : stores}
        
    
            
        