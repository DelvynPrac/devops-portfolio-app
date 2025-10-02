import pytest
from app.app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_routes(client):
    for path in ["/", "/about", "/healthz"]:
        res = client.get(path)
        assert res.status_code == 200