from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json(),200
        return {"message":"Store with name '{}' not found".format(name)},404

    def post(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return {"message:""A store with name '{}' already exists".format(name)},400
        else:
            store = StoreModel(name)
            try:
                StoreModel.save_to_db()
            except:
                return {"message ":"An error occured while creating the store"},500
        return store.json(),201

    def delete(self,name):
        store=StoreModel.find_by_name()
        if store:
            StoreModel.delete_from_db()

        return {"message":"Store Deleted"}

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all() ]}


