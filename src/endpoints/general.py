'''
General Endpoints
'''
from sanic import Blueprint
# from sanic.exceptions import *
from sanic.response import json
from src.errors import InputError, UnauthorizedError, ForbiddenError, NotFoundError, DataConflictError, UnprocessableEntityError
from src.wrappers import exception_wrapper

general = Blueprint('general', __name__)
#===============================================================================
# General
@general.route('/', methods=['GET'])
@exception_wrapper
def default(request):
    response = {'status': 'ok', 'message': '', 'payload': []}

    test_code = request.args.get('test', None)
    if test_code == '400': raise InputError('TEST')  # noqa: E701
    if test_code == '401': raise UnauthorizedError('TEST')  # noqa: E701
    if test_code == '403': raise ForbiddenError('TEST')  # noqa: E701
    if test_code == '404': raise NotFoundError('TEST')  # noqa: E701
    if test_code == '409': raise DataConflictError('TEST')  # noqa: E701
    if test_code == '422': raise UnprocessableEntityError('TEST')  # noqa: E701
    if test_code == '500': raise Exception('TEST')  # noqa: E701

    response['VERSION'] = request.app.config['VERSION']
    response['payload'] = []

    return json(response, status=200)
