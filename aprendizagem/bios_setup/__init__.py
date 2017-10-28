from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from bios_setup import configuration

app = Flask(__name__, static_url_path='', static_folder='frontend')
app.config.from_object('bios_setup:configuration')
db = SQLAlchemy(app)

import bios_setup.api.views
