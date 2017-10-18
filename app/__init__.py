from flask import Flask

APP = Flask(__name__, instance_relative_config=True)

from app import views

APP.config.from_object('config')