from app.catalog.views import catalog
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from app.assets.views import asset_blueprint
app = Flask(__name__)
app.register_blueprint(asset_blueprint)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

app.register_blueprint(catalog)
db.create_all()