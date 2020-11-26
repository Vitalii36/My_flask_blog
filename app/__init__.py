from flask import Flask
from conffig import Config
from . import forms

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
