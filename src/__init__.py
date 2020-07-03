'''
Main API Server
'''
#===============================================================================
import os
from sanic import Sanic
from sanic_cors import CORS
# from src.models import dbs/
from src.routes import build_blueprints
from src.util import bcolours
#===============================================================================
# API Creation & Configuration
def build_api():

    api_build = Sanic(__name__)
    CORS(api_build, supports_credentials=True)

    if 'ENV' not in os.environ:
        raise RuntimeError('Specify ENV for application: "development", "testing", or "production"')
    api_build.config['ENV'] = os.environ['ENV']
    if api_build.config['ENV'] == 'development':
        print(bcolours.OKGREEN + "\n %% DEV %% \n" + bcolours.ENDC)
        api_build.config.from_object('config.DevelopmentConfig')
    elif api_build.config['ENV'] == 'testing':
        print(bcolours.WARNING + "\n %% TEST %% \n" + bcolours.ENDC)
        api_build.config.from_object('config.TestingConfig')
    elif api_build.config['ENV'] == 'production':
        print(bcolours.OKBLUE + "\n %% PROD %% \n" + bcolours.ENDC)
        api_build.config.from_object('config.ProductionConfig')
    else:
        raise RuntimeError('CONFIGURATION STARTUP ERROR\nENV was not properly specified as one of "development", "testing", or "production".')

    # db.init_app(api_build)
    build_blueprints(api_build)
    return api_build

api = build_api()
