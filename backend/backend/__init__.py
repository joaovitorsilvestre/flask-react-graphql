from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_redis import FlaskRedis


app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'testing'}
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'flask+mongoengine=<3'
app.config['REDIS_URL'] = 'redis://127.0.0.1:6379'
app.debug = True

db = MongoEngine()
db.init_app(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

redis_store = FlaskRedis(app)

from backend import views
from backend.GraphqlSchema import schema