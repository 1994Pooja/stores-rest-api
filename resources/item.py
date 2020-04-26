from flask_jwt import jwt_required
from flask_restful import Resource,reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser();
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Store_id cannot be left empty")
    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":"Item Not found"},404



    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return{"message": "Item Name already exists"},400
        else:
            data=Item.parser.parse_args()
            item=ItemModel(name,data['price'],data['store_id'])
            try:
                item.save_to_db()
            except:
                return {"message: An error occured while inserting the items"},500
            return item.json(),201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.delete_from_db()
        return {'message':'Item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price=data['price']
        else:
             item=ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return item.json()

class ItemList(Resource):
    def get(self):
        # second way:::  return {'items':list(map(lambda x:x.json(),ItemModel.query.all()))}
        return {'items':[item.json() for item in ItemModel.query.all()]}
