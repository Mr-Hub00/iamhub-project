#!/usr/bin/env python3
"""
Test script for JWT Authentication endpoints
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_registration():
    """Test user registration endpoint"""
    url = f"{BASE_URL}/auth/registration/"
    data = {
        "username": "testchampion",
        "email": "test@champion.com", 
        "password1": "championpass123",
        "password2": "championpass123"
    }
    
    response = requests.post(url, data=data)
    print(f"🔐 Registration Status: {response.status_code}")
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Registration Success!")
        print(f"🎯 Access Token: {result.get('access_token', 'Not provided')[:50]}...")
        return result.get('access_token')
    else:
        print(f"❌ Registration Failed: {response.text}")
        return None

def test_login():
    """Test user login endpoint"""
    url = f"{BASE_URL}/auth/login/"
    data = {
        "username": "testchampion",
        "password": "championpass123"
    }
    
    response = requests.post(url, data=data)
    print(f"🔐 Login Status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Login Success!")
        print(f"🎯 Access Token: {result.get('access_token', 'Not provided')[:50]}...")
        return result.get('access_token')
    else:
        print(f"❌ Login Failed: {response.text}")
        return None

def test_user_profile(token):
    """Test getting user profile with JWT token"""
    url = f"{BASE_URL}/auth/user/"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    print(f"👤 User Profile Status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Profile Success!")
        print(f"📧 User: {result.get('username')} ({result.get('email')})")
        print(f"🏠 Wallet: {result.get('wallet_address', 'Not set')}")
        return result
    else:
        print(f"❌ Profile Failed: {response.text}")
        return None

if __name__ == "__main__":
    print("🚀 Testing IAMHub JWT Authentication System\n")
    
    # Test 1: Registration
    print("=" * 50)
    print("TEST 1: User Registration")
    token = test_registration()
    print()
    
    # Test 2: Login (if registration failed)
    if not token:
        print("=" * 50) 
        print("TEST 2: User Login")
        token = test_login()
        print()
    
    # Test 3: Protected endpoint
    if token:
        print("=" * 50)
        print("TEST 3: Protected User Profile")
        test_user_profile(token)
        print()
    
    print("=" * 50)
    print("🎯 JWT Authentication Test Complete!")
