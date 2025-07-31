import requests
import json

def pin_to_ipfs(file_path, ipfs_url='https://ipfs.infura.io:5001/api/v0'):
    """Pin a file to IPFS."""
    with open(file_path, 'rb') as file:
        response = requests.post(f'{ipfs_url}/add', files={'file': file})
        if response.status_code == 200:
            ipfs_hash = response.json()['Hash']
            print(f'File pinned to IPFS with hash: {ipfs_hash}')
            return ipfs_hash
        else:
            print('Error pinning file to IPFS:', response.text)
            return None

if __name__ == '__main__':
    # Example usage
    file_to_pin = 'path/to/your/file.txt'  # Replace with your file path
    pin_to_ipfs(file_to_pin)