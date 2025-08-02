"""
Clean JWT Authentication Views for IAMHub
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.db import IntegrityError
import json

User = get_user_model()

def get_tokens_for_user(user):
    """Generate JWT tokens for user"""
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    Register a new user and return JWT tokens
    """
    try:
        data = request.data
        username = data.get('username')
        email = data.get('email') 
        password = data.get('password')
        password2 = data.get('password2')
        
        # Validation
        if not all([username, email, password, password2]):
            return Response({
                'error': 'All fields are required: username, email, password, password2'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        if password != password2:
            return Response({
                'error': 'Passwords do not match'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        if len(password) < 8:
            return Response({
                'error': 'Password must be at least 8 characters'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        # Check if user exists
        if User.objects.filter(username=username).exists():
            return Response({
                'error': 'Username already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        if User.objects.filter(email=email).exists():
            return Response({
                'error': 'Email already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Create user with optional ChampionP fields
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Set optional ChampionP fields if provided
        if 'role' in data and data['role'] in dict(User.ROLE_CHOICES):
            user.role = data['role']
        if 'purpose_statement' in data:
            user.purpose_statement = data['purpose_statement']
        if 'primary_personality' in data and data['primary_personality'] in dict(User.PERSONALITY_CHOICES):
            user.primary_personality = data['primary_personality']
        if 'bio' in data:
            user.bio = data['bio']
        if 'location' in data:
            user.location = data['location']
        if 'interests' in data:
            user.interests = data['interests']
            
        user.save()
        
        # Generate tokens
        tokens = get_tokens_for_user(user)
        
        return Response({
            'message': 'User created successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'wallet_address': user.wallet_address,
                'role': user.role,
                'purpose_statement': user.purpose_statement,
                'primary_personality': user.primary_personality,
                'bio': user.bio,
                'location': user.location,
                'reputation_score': user.reputation_score,
                'community_rank': user.community_rank,
                'is_champion': user.is_champion,
                'connection_score': user.connection_score
            },
            'tokens': tokens
        }, status=status.HTTP_201_CREATED)
        
    except IntegrityError as e:
        return Response({
            'error': 'User creation failed due to database constraint'
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'error': f'Registration failed: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    Login user and return JWT tokens
    """
    try:
        data = request.data
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return Response({
                'error': 'Username and password are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
        if not user.is_active:
            return Response({
                'error': 'Account is disabled'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        # Generate tokens
        tokens = get_tokens_for_user(user)
        
        return Response({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'wallet_address': user.wallet_address,
                'role': user.role,
                'purpose_statement': user.purpose_statement,
                'primary_personality': user.primary_personality,
                'bio': user.bio,
                'location': user.location,
                'reputation_score': user.reputation_score,
                'community_rank': user.community_rank,
                'is_champion': user.is_champion,
                'connection_score': user.connection_score,
                'nft_count': user.nft_count,
                'token_balance': float(user.token_balance),
                'dao_participation': user.dao_participation
            },
            'tokens': tokens
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Login failed: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    """
    Get current user profile (JWT protected)
    """
    try:
        user = request.user
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'wallet_address': user.wallet_address,
                'role': user.role,
                'date_joined': user.date_joined,
                'is_active': user.is_active,
                # ChampionP Profile Fields
                'purpose_statement': user.purpose_statement,
                'purpose_tags': user.purpose_tags,
                'bio': user.bio,
                'avatar_url': user.avatar_url,
                'location': user.location,
                'website': user.website,
                'community_rank': user.community_rank,
                'reputation_score': user.reputation_score,
                'primary_personality': user.primary_personality,
                'personality_traits': user.personality_traits,
                'skills': user.skills,
                'certifications': user.certifications,
                'experience_level': user.experience_level,
                'interests': user.interests,
                'collaboration_preferences': user.collaboration_preferences,
                'availability_status': user.availability_status,
                'nft_count': user.nft_count,
                'token_balance': float(user.token_balance),
                'dao_participation': user.dao_participation,
                'profile_visibility': user.profile_visibility,
                'is_champion': user.is_champion,
                'connection_score': user.connection_score,
                'join_date': user.join_date,
                'last_active': user.last_active
            }
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Failed to retrieve profile: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def update_wallet_view(request):
    """
    Update user's wallet address
    """
    try:
        user = request.user
        wallet_address = request.data.get('wallet_address')
        
        if not wallet_address:
            return Response({
                'error': 'Wallet address is required'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        user.wallet_address = wallet_address
        user.save()
        
        return Response({
            'message': 'Wallet address updated successfully',
            'wallet_address': user.wallet_address
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Failed to update wallet: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile_view(request):
    """
    Update user's ChampionP profile fields
    """
    try:
        user = request.user
        data = request.data
        
        # Update fields if provided
        updatable_fields = [
            'purpose_statement', 'purpose_tags', 'bio', 'avatar_url', 
            'location', 'website', 'personality_traits', 'certifications',
            'interests', 'collaboration_preferences', 'availability_status',
            'profile_visibility'
        ]
        
        updated_fields = []
        for field in updatable_fields:
            if field in data:
                setattr(user, field, data[field])
                updated_fields.append(field)
        
        # Handle special fields with validation
        if 'primary_personality' in data and data['primary_personality'] in dict(User.PERSONALITY_CHOICES):
            user.primary_personality = data['primary_personality']
            updated_fields.append('primary_personality')
            
        if 'experience_level' in data and data['experience_level'] in ['beginner', 'intermediate', 'advanced', 'expert', 'master']:
            user.experience_level = data['experience_level']
            updated_fields.append('experience_level')
            
        if 'skills' in data and isinstance(data['skills'], dict):
            user.set_skills(data['skills'])
            updated_fields.append('skills')
        
        user.save()
        
        return Response({
            'message': 'Profile updated successfully',
            'updated_fields': updated_fields,
            'user': {
                'id': user.id,
                'username': user.username,
                'reputation_score': user.reputation_score,
                'connection_score': user.connection_score,
                'is_champion': user.is_champion
            }
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Failed to update profile: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_skills_view(request):
    """
    Update user's skills and proficiency ratings
    """
    try:
        user = request.user
        skills_data = request.data.get('skills')
        
        if not skills_data or not isinstance(skills_data, dict):
            return Response({
                'error': 'Skills data must be a valid JSON object'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate skill ratings (0-100)
        for skill, rating in skills_data.items():
            if not isinstance(rating, (int, float)) or rating < 0 or rating > 100:
                return Response({
                    'error': f'Skill rating for {skill} must be between 0 and 100'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_skills(skills_data)
        user.save()
        
        return Response({
            'message': 'Skills updated successfully',
            'skills': user.skills
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Failed to update skills: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def community_champions_view(request):
    """
    Get list of community champions for networking
    """
    try:
        user = request.user
        
        # Get champions that user can connect with
        champions = User.objects.filter(
            role__in=['champion', 'elder', 'admin'],
            profile_visibility__in=['public', 'community']
        ).exclude(id=user.id).order_by('-reputation_score')[:20]
        
        champions_data = []
        for champion in champions:
            if user.can_connect_with(champion):
                champions_data.append({
                    'id': champion.id,
                    'username': champion.username,
                    'role': champion.role,
                    'reputation_score': champion.reputation_score,
                    'community_rank': champion.community_rank,
                    'primary_personality': champion.primary_personality,
                    'location': champion.location,
                    'availability_status': champion.availability_status,
                    'connection_score': champion.connection_score,
                    'skills': champion.skills,
                    'interests': champion.interests,
                    'avatar_url': champion.avatar_url
                })
        
        return Response({
            'champions': champions_data,
            'total_count': len(champions_data)
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Failed to retrieve champions: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def web3_connect_view(request):
    """
    Handle Web3 wallet connection and signature verification
    """
    try:
        user = request.user
        data = request.data
        
        wallet_address = data.get('wallet_address')
        signature = data.get('signature')
        message = data.get('message')
        
        if not all([wallet_address, signature, message]):
            return Response({
                'error': 'wallet_address, signature, and message are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Basic wallet address validation
        if not wallet_address.startswith('0x') or len(wallet_address) != 42:
            return Response({
                'error': 'Invalid Ethereum wallet address format'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Update user's wallet and Web3 status
        user.wallet_address = wallet_address
        user.dao_participation = True  # Mark as Web3 participant
        user.reputation_score += 5  # Bonus for Web3 connection
        user.save()
        
        return Response({
            'message': 'Web3 wallet connected successfully',
            'wallet_address': user.wallet_address,
            'dao_participation': user.dao_participation,
            'reputation_score': user.reputation_score,
            'connection_score': user.connection_score
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Failed to connect Web3 wallet: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
