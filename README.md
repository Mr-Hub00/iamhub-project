# IAMHub Project

## Overview
IAMHub is a comprehensive project that integrates a Django backend with a frontend interface, smart contracts for NFT management, and IPFS for decentralized storage. This project aims to provide a seamless experience for users to upload, mint, and manage NFTs while ensuring robust user authentication and administrative functionalities.

## Project Structure
```
iamhub-project/
├── backend/                         # Django Project Root
│   ├── iamhub/                      # Django core app
│   │   ├── settings.py               # Project settings
│   │   ├── urls.py                   # URL routing
│   │   └── wsgi.py                   # WSGI entry point
│   ├── manage.py                     # Command-line utility for Django
│   └── apps/
│       ├── nft_upload/               # Upload + mint NFT app
│       ├── users/                    # Auth, roles, profile handling
│       └── dashboard/                # Admin panel views
│
├── frontend/                        # Optional frontend for Astro/static
│   ├── index.html                    # Main HTML file
│   └── styles/
│       └── main.css                 # CSS styles
│
├── smart_contracts/                 # PeaceToken, ERC721, etc.
│   ├── PeaceToken.sol                # Solidity smart contract
│   └── deploy_scripts/
│       └── deploy_peacetoken.js      # Deployment script
│
├── ipfs_upload/                     # IPFS integration
│   └── pin_to_ipfs.py               # Script to pin files to IPFS
│
├── .github/
│   └── workflows/
│       └── mint_nft.yml             # GitHub Actions automation
│
├── README.md                        # Project documentation
└── requirements.txt                 # Python dependencies
```

## Setup Instructions

### Backend
1. Navigate to the `backend` directory.
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

### Frontend
1. Navigate to the `frontend` directory.
2. Use your preferred static site generator to build the frontend.

### Smart Contracts
1. Navigate to the `smart_contracts` directory.
2. Use Truffle or Hardhat to compile and deploy the smart contracts.

### IPFS Integration
1. Ensure you have IPFS installed and running.
2. Use the `pin_to_ipfs.py` script to pin files to IPFS.

## Usage
- Access the Django application at `http://127.0.0.1:8000/`.
- Use the frontend to interact with the backend and smart contracts.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.