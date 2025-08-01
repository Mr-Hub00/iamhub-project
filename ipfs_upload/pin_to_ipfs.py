import os
import requests
from dotenv import load_dotenv

load_dotenv()

STORACHA_API_KEY = os.getenv("STORACHA_API_KEY")
STORACHA_SECRET_KEY = os.getenv("STORACHA_SECRET_KEY")
STORACHA_UPLOAD_URL = os.getenv("STORACHA_UPLOAD_URL", "https://api.storacha.com/api/v0/upload")

def pin_file_to_ipfs(filepath):
    if not STORACHA_API_KEY or not STORACHA_SECRET_KEY:
        raise EnvironmentError("Storacha API keys not set in .env file.")

    headers = {
        "Authorization": f"Bearer {STORACHA_API_KEY}:{STORACHA_SECRET_KEY}"
    }

    with open(filepath, "rb") as file_data:
        files = {"file": file_data}
        response = requests.post(STORACHA_UPLOAD_URL, files=files, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Storacha upload failed: {response.status_code} {response.text}")

    data = response.json()
    return data.get("cid") or data.get("IpfsHash")  # Adjust if needed per Storacha's spec

def pin_json_to_ipfs(json_data):
    url = "https://api.storacha.com/v1/pins/json"
    headers = {
        "Authorization": f"Bearer {STORACHA_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=json_data, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Storacha JSON pin failed: {response.status_code} {response.text}")
    
    return response.json().get("cid")

# Example usage
if __name__ == "__main__":
    sample_path = "backend/apps/nft_upload/test_upload/sample.jpg"  # Change this to your test file
    cid = pin_file_to_ipfs(sample_path)
    print(f"✅ Uploaded to IPFS. CID: {cid}")