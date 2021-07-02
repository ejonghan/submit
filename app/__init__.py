from app.main.index import main as main
from flask import Flask

app = Flask(__name__)

app.register_blueprint(main)
