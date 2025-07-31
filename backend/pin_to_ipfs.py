import requests

STORACHA_API_KEY = 'YOUR_STORACHA_API_KEY'
STORACHA_API_SECRET = 'YOUR_STORACHA_API_SECRET'

def pin_file_to_ipfs(filepath):
    url = "https://api.storacha.com/v1/pins/file"
    headers = {
        "Authorization": f"Bearer {STORACHA_API_KEY}",
        # Add any other required headers here
    }
    with open(filepath, "rb") as fp:
        files = {"file": fp}
        response = requests.post(url, files=files, headers=headers)
    response.raise_for_status()
    return response.json()["cid"]

def pin_json_to_ipfs(json_data):
    url = "https://api.storacha.com/v1/pins/json"
    headers = {
        "Authorization": f"Bearer {STORACHA_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=json_data, headers=headers)
    response.raise_for_status()
    return response.json()["cid"]

if __name__ == '__main__':
    # Example usage
    file_to_pin = 'path/to/your/file.txt'  # Replace with your file path
    pin_file_to_ipfs(file_to_pin)