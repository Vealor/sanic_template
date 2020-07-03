
from sanic.response import json
from sanic.exceptions import SanicException

#===============================================================================
### Endpoint Imports
def build_blueprints(api):

    # General Endpoints
    from src.endpoints.general import general  # noqa: E402
    api.blueprint(general, url_prefix='/')

    # Auth Endpoints
    from src.endpoints.auth import auth  # noqa: E402
    api.register_blueprint(auth, url_prefix='/auth')

    # User Endpoints
    from src.endpoints.users import users  # noqa: E402
    api.register_blueprint(users, url_prefix='/users')

    #===============================================================================
    # Error Handling

    @api.exception(SanicException)
    async def http_error_handler(request, exception):
        return json({'status': 'error', 'payload': [], 'message': exception.args}, status=exception.status_code)
