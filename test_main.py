from fastapi.testclient import TestClient
from main import app
client=TestClient(app)

def test_say_hello():
    result=client.get("/say/hello")
    assert result.status_code==200
    assert result.json()=={"message":15}
# def test_generate_result():
#     response=client.get("/say/add/5/10")
#     assert response.json()=={"result":15}