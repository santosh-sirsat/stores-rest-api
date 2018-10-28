from flask import Flask;
from flask_restful import Api;
from flask_jwt import JWT

from security import authenticate, identity

from resources.user import UserRegister; #here user is file name and UserRegister is class name on that file
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__);


#start :: SQLALCHEMY param setting
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
#end:: SQLALCHEMY param setting

app.secret_key = 'jose';
api = Api(app);

@app.before_first_request
def create_tables():
    db.create_all();
from resources.store import Store, StoreList;

jwt = JWT(app, authenticate, identity)# create new end point /auth

api.add_resource(Store, '/store/<string:name>');# http://127.0.0.1:5000/store/Dell-store
api.add_resource(Item, '/item/<string:name>'); # http://127.0.0.1:5000/item/Dell-laptop
api.add_resource(ItemList, '/items'); # http://127.0.0.1:5000/items
api.add_resource(UserRegister, '/register'); # http://127.0.0.1:5000/register
api.add_resource(StoreList, '/stores'); # http://127.0.0.1:5000/stores

if __name__ == '__main__':
    from db import db;
    db.init_app(app)
    app.run(port=5000, debug = True);
