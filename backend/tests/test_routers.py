from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_token_generation():
    tokens = [client.get("/generate_token").json() for _ in range(20)]
    for token in tokens:
        assert len(token) == 4
    assert len(set(tokens)) == len(tokens)
