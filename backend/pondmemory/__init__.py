from flask import Flask 
from flask_cors import CORS
import config
import pondmemory.user.user as user
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object(config)
    app.register_blueprint(user.bp)

    return app

app = create_app()

# from pondmemory.database.Mongo import Mongo
# print(Mongo().insert_one("User", {"username": "killuayz", "password": "<PASSWORD>"}))
# Mongo().delete_many("User",{"username": "killuayz"})
# res = Mongo().find_one("User", {"username": "xinxin"})
# print(res)
# print(res["username"])
