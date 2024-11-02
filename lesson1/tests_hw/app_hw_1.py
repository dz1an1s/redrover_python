import requests

URL = "http://127.0.0.1:8000/testcases/"

data = {
  "id": 22,
  "name": "Guru",
  "description": "string",
  "steps": [
    "string"
  ],
  "expected_result": "string",
  "priority": "низкий"
}
def test_get_cases():
    response = requests.get(URL)

    # print(response.json())

def test_post_new_case():
    response = requests.post(URL, json=data)
    assert response.json()["id"] == 22
    # print(response.json()["id"])