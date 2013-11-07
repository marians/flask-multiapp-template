from flask import Flask
app = Flask(__name__)

from model import MyModel
model = MyModel()

import views
