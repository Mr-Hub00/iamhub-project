import os
import requests
from dotenv import load_dotenv

load_dotenv()

STORACHA_API_KEY = os.getenv("STORACHA_API_KEY")
STORACHA_SECRET_KEY = os.getenv("STORACHA_SECRET_KEY")
STORACHA_UPLOAD_URL = os.getenv("STORACHA_UPLOAD_URL", "https://api.storacha.com/api/v0/upload")

def pin_file_to_ipfs(filepath):
    headers = {
        "Authorization": f"Bearer {STORACHA_API_KEY}:{STORACHA_SECRET_KEY}"
    }

    with open(filepath, "rb") as file_data:
        files = {"file": file_data}
        response = requests.post(STORACHA_UPLOAD_URL, files=files, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Storacha upload failed: {response.status_code} {response.text}")

    data = response.json()
    return data.get("cid")  # or "IpfsHash" depending on Storacha's response structure

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