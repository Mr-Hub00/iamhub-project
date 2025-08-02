# IAMHub Authentication System

## Overview
IAMHub now features a complete JWT-based authentication system with a modern frontend interface. The system bypasses the compatibility issues with dj-rest-auth by implementing custom JWT authentication views.

## Features
- ✅ Custom JWT Authentication (Access & Refresh tokens)
- ✅ User Registration with email validation
- ✅ User Login with username/email support
- ✅ Wallet Address Management
- ✅ Modern Frontend Templates
- ✅ Cross-Origin Resource Sharing (CORS) support
- ✅ Token-based API access

## Quick Start

### 1. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r ../requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

### 2. Frontend Access
Open the following files in your browser:
- **Registration**: `frontend/register.html`
- **Login**: `frontend/login.html` 
- **Dashboard**: `frontend/dashboard.html`

## API Endpoints

### Authentication Endpoints
All authentication endpoints are prefixed with `/api/auth/`

#### Register User
- **POST** `/api/auth/register/`
- **Body**: 
```json
{
    "username": "your_username",
    "email": "your@email.com", 
    "password": "your_password",
    "password2": "your_password"
}
```
- **Response**: JWT tokens + user data

#### Login User
- **POST** `/api/auth/login/`
- **Body**:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
- **Response**: JWT tokens + user data

#### Get User Profile
- **GET** `/api/auth/profile/`
- **Headers**: `Authorization: Bearer <access_token>`
- **Response**: User profile data

#### Update Wallet Address
- **POST** `/api/auth/update-wallet/`
- **Headers**: `Authorization: Bearer <access_token>`
- **Body**:
```json
{
    "wallet_address": "0x1234567890123456789012345678901234567890"
}
```

## Frontend Features

### Register Page (`register.html`)
- Modern UI with form validation
- Real-time password confirmation
- Automatic redirect to dashboard on success
- Comprehensive error handling

### Login Page (`login.html`)  
- Clean authentication interface
- JWT token storage in localStorage
- User dashboard display after login
- Wallet address update functionality

### Dashboard (`dashboard.html`)
- Protected route (requires authentication)
- User profile display
- Wallet connection management
- Activity statistics (placeholder)
- Quick action buttons

## Technical Details

### Authentication Flow
1. User registers/logs in via frontend
2. Backend validates credentials
3. JWT tokens returned (access + refresh)
4. Frontend stores tokens in localStorage
5. Subsequent API calls include Bearer token
6. Backend validates token for protected routes

### Token Management
- **Access Token**: 60 minutes lifetime
- **Refresh Token**: 7 days lifetime
- **Automatic Rotation**: Enabled
- **Blacklist Support**: Yes

### Security Features
- CSRF protection
- CORS configuration for frontend
- Password validation
- JWT token rotation
- Secure token storage

## Project Structure
```
frontend/
├── register.html     # User registration page
├── login.html        # User login page
└── dashboard.html    # Main user dashboard

backend/
├── apps/users/
│   ├── api_views.py  # Custom JWT authentication views
│   ├── urls.py       # Authentication URL patterns
│   ├── models.py     # CustomUser model
│   └── ...
└── iamhub/
    ├── settings.py   # Django configuration
    ├── urls.py       # Main URL routing
    └── ...
```

## Troubleshooting

### Common Issues

1. **CORS Errors**: Make sure Django server is running and CORS is configured
2. **Token Errors**: Check if tokens are properly stored in localStorage
3. **Network Errors**: Verify API endpoints are accessible at `http://127.0.0.1:8000`

### Development Notes
- The system uses Django 4.2 with custom user model
- JWT implementation via djangorestframework-simplejwt
- No dependency on dj-rest-auth (resolved compatibility issues)
- Frontend uses vanilla JavaScript (no frameworks)

## Next Steps
- [ ] Add user profile editing
- [ ] Implement NFT upload integration
- [ ] Add real-time wallet connection via Web3
- [ ] Enhanced error handling and validation
- [ ] Add user roles and permissions
- [ ] Implement password reset functionality

## Testing

The system has been tested with:
- User registration via API
- User login via API
- JWT token generation and validation
- Frontend authentication flow
- Wallet address updates

## Support
For issues or questions, check the Django server logs and browser console for detailed error messages.
