import pytest
from test._helpers import get_req
from test import api, test_client

@pytest.mark.general
class TestGeneralGet:
    async def test_health_version_success(self, test_client):
        response = await get_req("/", test_client)
        async with response:
            assert response.status == 200
            data = await response.json()
            assert data.get("status") == "ok"
            assert "VERSION" in data.keys()


@pytest.mark.general
class TestFailuresGet:
    async def test_400(self, test_client):
        response = await get_req("/?test=400", test_client)
        async with response:
            assert response.status == 400
            data = await response.json()
            assert data.get("status") == "error"

    async def test_401(self, test_client):
        response = await get_req("/?test=401", test_client)
        async with response:
            assert response.status == 401
            data = await response.json()
            assert data.get("status") == "error"

    async def test_403(self, test_client):
        response = await get_req("/?test=403", test_client)
        async with response:
            assert response.status == 403
            data = await response.json()
            assert data.get("status") == "error"

    async def test_404(self, test_client):
        response = await get_req("/?test=404", test_client)
        async with response:
            assert response.status == 404
            data = await response.json()
            assert data.get("status") == "error"

    async def test_409(self, test_client):
        response = await get_req("/?test=409", test_client)
        async with response:
            assert response.status == 409
            data = await response.json()
            assert data.get("status") == "error"

    async def test_422(self, test_client):
        response = await get_req("/?test=422", test_client)
        async with response:
            assert response.status == 422
            data = await response.json()
            assert data.get("status") == "error"

    async def test_500(self, test_client):
        response = await get_req("/?test=500", test_client)
        async with response:
            assert response.status == 500
            data = await response.json()
            assert data.get("status") == "error"
