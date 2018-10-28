from flask_restful import Resource,reqparse;
from models.store import StoreModel;

class Store(Resource):
    parser = reqparse.RequestParser();
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json();
        return {'message','Store not found'}, 400

    def post(self, name):
        store = StoreModel.find_by_name(name);
        if store:
            return {'message':"A store with name '{}' already exists".format(name)};
        else:
            data = self.parser.parse_args();
        #data = request.get_json();
        #item = ItemModel(name, data['price'], data['store_id']);
            store = StoreModel(name);
        try:
            store.save_to_db();
        except:
            return {'message' : 'An error occurred while creating the store'}; 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name);
        if store:
            store.delete_from_db();
        return {'message':'Store deleted'}

class StoreList(Resource):
    def get(self):
        return { 'stores': [store.json() for store in StoreModel.query.all()] }; #list comprihension
        #return { 'stores': list(map(lambda x: x.json(), StoreModel.query.all())) }; # lambda
