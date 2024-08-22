import requests

URL = "http://127.0.0.1:8081"

CHAT_API_ENDPOINT = f"{URL}/api/completion"

def chat_completion_request(content):
    headers = {'Content-type': 'application/json'}
    data = {'content': content}

    try:
        req = requests.post(url=CHAT_API_ENDPOINT, headers=headers, json=data)
        req.raise_for_status()  # Raise an exception for bad status codes
        json_extracted = req.text
        print("Response status code:", req.status_code)  # Debug print
        print("Response content:", json_extracted[:100] + "...")  # Print first 100 chars
        return json_extracted
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        raise