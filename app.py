from flask import Flask, render_template, request, redirect, url_for, session
from backend.models.basic_models import *

app = Flask(__name__)

app.config.from_object('backend.models.config')
db = db_setup(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
