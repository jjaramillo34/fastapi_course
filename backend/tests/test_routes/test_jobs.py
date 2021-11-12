import json


def test_create_job(client, normal_user_token_headers):
#def test_create_job(client):
    data = {
        "title":"SDE 1 Yahoo",
        "company":"testhoo",
        "company_url":"https://wwww.fdj.com",
        "location":"USA,NY",
        "description":"Testing",
        "date_posted":"2021-07-20"
    }
    response = client.post("/job/create-job",json.dumps(data),headers=normal_user_token_headers)
    #response = client.post("/job/create-job",json.dumps(data))
    assert response.status_code == 200


def test_retreive_job_by_id(client,normal_user_token_headers):
#def test_retreive_job_by_id(client):
    data = {
        "title":"SDE 1 Yahoo",
        "company":"testhoo",
        "company_url":"https://wwww.fdj.com",
        "location":"USA,NY",
        "description":"Testing",
        "date_posted":"2021-07-20"
    }
    client.post("/job/create-job",json.dumps(data),headers=normal_user_token_headers)
    #client.post("/job/create-job",json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"

