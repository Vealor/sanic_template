'''
General Endpoints
'''
from sanic import Blueprint
# from sanic.exceptions import *
from sanic.response import json
# from src.errors import *
from src.wrappers import exception_wrapper

general = Blueprint('general', __name__)
#===============================================================================
# General
@general.route('/', methods=['GET'])
@exception_wrapper
def default(request, id=None):
    response = {'status': 'ok', 'message': '', 'payload': []}

    response['VERSION'] = request.app.config['VERSION']
    response['payload'] = []

    return json(response, status=200)
