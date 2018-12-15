import requests
import json

def test_add():
    data = {
        "title", "title",
        "content", "content"
    }
    res = requests.post("http://127.0.0.1:8888/add/", json=data)
    print(res.status_code)
    print(json.loads(res.text))

if __name__ == '__main__':
    test_add()