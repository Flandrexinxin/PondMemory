from flask import Flask 
from flask_cors import CORS
import config
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object(config)

    return app

app = create_app()