import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jovy'
api = Api(app)


jwt = JWT(app, authenticate, identity)

# 200 -->OK (Quando il server può ritornare alcuni dati)
# 404 -->NOT FOUND (Valore non trovato)
# 201 -->CREATED (Quando un nuovo oggetto è stato creato a aggiunto al db)
# 202 -->ACCEPTED (Quando stiamo ritardando la creazione e l'oggetto sarà creato dopo qualche minuto)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug = True)
