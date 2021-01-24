import os
from flask import Flask, request
from flask_cors import CORS
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from functools import wraps

authorizations = {
  'apikey': {
    'type': 'apiKey',
    'in': 'header',
    'name': 'X-API-KEY'
  }
}

db = SQLAlchemy()
ma = Marshmallow()
api = Api(version='0.0.1', title='Flask Microservice',
  description='Python Flask Microservice API REST',
  authorizations=authorizations
)

def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = None
    if 'X-API-KEY' in request.headers:
      token = request.headers['X-API-KEY']
    if not token:
      return {'success': False, 'message': 'Token is missing.'}, 401
    if token not in [os.getenv('API_KEY', 'zz6ae7aainheq2ysz9$a8qjyedg65c50')]:
      return {'success': False, 'message': 'Token is wrong.'}, 401
    return f(*args, **kwargs)
  return decorated

apins = api.namespace('api', description='API')

@api.errorhandler(Exception)
def default_error_handler(error):
  '''Default error handler'''
  return {'success': False, 'message': str(error)}, getattr(error, 'code', 500)

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', '')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  CORS(app)

  db.init_app(app)
  ma.init_app(app)
  api.init_app(app)

  with app.app_context():
    db.create_all()

  # Registro de los Blueprints
  from .index import indexbp
  app.register_blueprint(indexbp)
  from .books import booksbp
  app.register_blueprint(booksbp)

  return app