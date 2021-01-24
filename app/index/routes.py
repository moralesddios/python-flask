from flask_restplus import Resource
from app import api

@api.route('/health')
class Health(Resource):
  def get(self):
    '''Test microservice health on this path'''
    return {'success': True, 'status': "OK"}
