'''
Created on Sep 28, 2017

@author: bhatsubh
'''
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item_model import ItemModel

class Item(Resource):
   
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be blank,should include the price of the item"
    )
   
    parser.add_argument('store_id',
            type=int,
            required=True,
            help="Every item needs a store id"
    )
     
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message" : "no such item exists"},404
        
    @jwt_required()
    def post(self,name):
        item = ItemModel.find_by_name(name)
        if not item:
            request_data = Item.parser.parse_args()
            new_item = {
                        'name' : name,
                        'price' : request_data['price'],
                        'store_id' : request_data['store_id']
                }
            new_item_obj = ItemModel(new_item['name'],new_item['price'],new_item['store_id'])
            new_item_obj.save_to_db()
            return {'item' : new_item_obj.json() },201
        else:
            return {"message" : "An item with that name already exists"},400
        
      
    @jwt_required()
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message" : "Item has been deleted"},201
        
    @jwt_required()
    def put(self,name):
        request_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = request_data['price']
        else:
            item = ItemModel(name,request_data['price'],request_data['store_id'])
        item.save_to_db()
        
        return {'item' : item.json()}
        
class ItemList(Resource):
    def get(self):
        items = []
        for item in ItemModel.query.all():
            items.append(item.json())
        return {"items" 
                : items},200