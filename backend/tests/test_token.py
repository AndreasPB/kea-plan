from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_token_generate():
    tokens = [client.get("/token/generate").json() for _ in range(20)]
    for token in tokens:
        assert len(token) == 4
    assert len(set(tokens)) == len(tokens)
