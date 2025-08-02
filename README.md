# IAMHub Project - ChampionP Identity Platform

## 🏆 Overview
IAMHub is a **revolutionary identity and community platform** that integrates a Django backend with advanced **ChampionP Framework**, Web3 wallet integration, smart contracts for NFT management, and IPFS for decentralized storage. This project provides a comprehensive experience for users to manage their sovereign identity, upload NFTs, connect Web3 wallets, and participate in community governance.

### 🚀 **Key Features**
- **🎯 ChampionP Framework** - 6-pillar identity system (Purpose, Profile, Placement, Personality, Proficiency, Potential Connections)
- **🔐 JWT Authentication** - Secure token-based authentication with refresh
- **🌐 Web3 Integration** - Metamask wallet connection and blockchain interaction
- **🎨 NFT Management** - Upload, mint, and manage NFT assets
- **🤝 Community Features** - Champion discovery and networking
- **⚡ Skills System** - Dynamic proficiency tracking and ratings
- **🏆 Reputation System** - Community scoring and ranking algorithms

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
4. Run database migrations to set up the ChampionP identity system:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```
6. Start the development server:
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

### ChampionP Identity System
- Access the Django application at `http://127.0.0.1:8000/`
- Create your ChampionP profile at `/champion-profile/`
- Connect your Metamask wallet for Web3 features
- Complete your 6-pillar identity assessment:
  - **Purpose**: Define your mission and values
  - **Profile**: Personal information and background
  - **Placement**: Location and professional context
  - **Personality**: MBTI type and traits
  - **Proficiency**: Skills and expertise levels
  - **Potential Connections**: Network and collaboration preferences

### API Endpoints
- `/api/register/` - Register new user
- `/api/login/` - JWT authentication
- `/api/profile/` - View/update profile
- `/api/update-skills/` - Manage skills
- `/api/community-champions/` - Discover champions
- `/api/web3-connect/` - Web3 wallet integration

### Frontend Features
- Modern responsive design
- Real-time profile editing
- Skills management system
- Community discovery
- Metamask integration

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

git remote add origin https://github.com/Mr-Hub00/iamhub-project.git
git branch -M main
git push -u origin main

How to check and change directory

To see your current folder, type:
pwd

To list files/folders in your current folder:
dir

To move into the backend folder:
cd backend

cd ..

cd frontend

python manage.py runserver

Use pwd to check your current folder.
Use cd foldername to move into a folder.
Use cd .. to move up one level.

python manage.py makemigrations
python manage.py migrate