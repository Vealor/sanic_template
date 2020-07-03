import pytest
# from ._helpers import seed_db_data
from src import build_api  # , db


@pytest.yield_fixture(scope="module")
def api(request):
    api = build_api()
    yield api
    # with api.app_context():
    #     if not request.config.getoption("--nodb"):
    #         print("\n\033[35mDROPPING DATABASE AND RESEED\033[0m\n")
    #         db.drop_all()
    #         db.create_all()
    #         seed_db_data()
    #     else:
    #         print("\n\033[33mDatabase Not Dropped\033[0m\n")
    #
    #     db.session.remove()


@pytest.fixture(scope="function")
def test_client(loop, api, sanic_client):
    return loop.run_until_complete(sanic_client(api))
