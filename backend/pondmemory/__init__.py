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
#
from pondmemory.utils.file import uploadFileToDB, getFileFromDB
# with open("C:\\Users\\killuayz\\Desktop\\微信图片_20240211233055.png", 'rb') as f:
#     uploadFileToDB(f.read(), "pic1", 'png')

# with open("./test.png", "wb") as f:
#     res = getFileFromDB({"fileName": "pic1"})
#     if(res is not None):
#         f.write(res["fileContent"])
#         res.pop("fileContent")
#         print(f"[DEBUG] {res}")


