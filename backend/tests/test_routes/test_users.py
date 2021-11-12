import json 


def test_create_user(client):
    data = {"username":"testusername","email":"abc@test.com","password":"1234556"}
    response = client.post("/users/",json.dumps(data))
    print(response.text)
    assert response.status_code == 200
    assert response.json()['email'] == "abc@test.com"
    assert response.json()["is_active"] == True