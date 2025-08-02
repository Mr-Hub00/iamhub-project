from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import json

class CustomUser(AbstractUser):
    # Core Identity Fields
    wallet_address = models.CharField(max_length=255, blank=True, null=True, 
                                    help_text="Ethereum wallet address for Web3 interactions")
    
    # Enhanced Role System
    ROLE_CHOICES = (
        ('champion', 'Champion'),           # Elite community leaders
        ('elder', 'Elder'),                 # Wise advisors
        ('creator', 'Creator'),             # Content creators
        ('builder', 'Builder'),             # Developers/builders
        ('guardian', 'Guardian'),           # Community moderators
        ('seeker', 'Seeker'),              # New members
        ('admin', 'Admin'),                 # System administrators
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='seeker')
    
    # ChampionP Framework Fields
    
    # 1. PURPOSE - Core Mission & Vision
    purpose_statement = models.TextField(max_length=500, blank=True, 
                                       help_text="Your core mission and purpose in the community")
    purpose_tags = models.CharField(max_length=300, blank=True,
                                  help_text="Comma-separated tags (e.g., peace, innovation, art)")
    
    # 2. PROFILE - Detailed Identity
    bio = models.TextField(max_length=1000, blank=True, 
                          help_text="Detailed biography and background")
    avatar_url = models.URLField(blank=True, help_text="Profile picture URL or IPFS hash")
    location = models.CharField(max_length=100, blank=True, help_text="Geographic location")
    website = models.URLField(blank=True, help_text="Personal website or portfolio")
    
    # 3. PLACEMENT - Community Position
    community_rank = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)],
                                       help_text="Community ranking (1-100)")
    reputation_score = models.IntegerField(default=0, help_text="Community reputation points")
    join_date = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    
    # 4. PERSONALITY - Traits & Characteristics
    PERSONALITY_CHOICES = (
        ('innovator', 'Innovator'),
        ('collaborator', 'Collaborator'),
        ('mentor', 'Mentor'),
        ('explorer', 'Explorer'),
        ('peacemaker', 'Peacemaker'),
        ('visionary', 'Visionary'),
        ('technologist', 'Technologist'),
        ('artist', 'Artist'),
    )
    primary_personality = models.CharField(max_length=20, choices=PERSONALITY_CHOICES, 
                                         blank=True, help_text="Primary personality type")
    personality_traits = models.CharField(max_length=300, blank=True,
                                        help_text="Additional personality traits (comma-separated)")
    
    # 5. PROFICIENCY - Skills & Expertise
    skills_json = models.TextField(blank=True, help_text="JSON object storing skill ratings")
    certifications = models.TextField(blank=True, help_text="Professional certifications and achievements")
    experience_level = models.CharField(max_length=20, choices=(
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'), 
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
        ('master', 'Master'),
    ), default='beginner')
    
    # 6. POTENTIAL CONNECTIONS - Networking
    interests = models.CharField(max_length=500, blank=True,
                               help_text="Areas of interest (comma-separated)")
    collaboration_preferences = models.CharField(max_length=300, blank=True,
                                               help_text="Preferred collaboration types")
    availability_status = models.CharField(max_length=20, choices=(
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('focused', 'Focused'),
        ('away', 'Away'),
    ), default='available')
    
    # Web3 & Blockchain Fields
    nft_count = models.IntegerField(default=0, help_text="Number of NFTs owned/created")
    token_balance = models.DecimalField(max_digits=20, decimal_places=8, default=0,
                                      help_text="PeaceToken balance")
    dao_participation = models.BooleanField(default=False, help_text="Active in DAO governance")
    
    # Privacy & Preferences
    profile_visibility = models.CharField(max_length=20, choices=(
        ('public', 'Public'),
        ('community', 'Community Only'),
        ('private', 'Private'),
    ), default='community')
    email_notifications = models.BooleanField(default=True)
    web3_notifications = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-reputation_score', '-last_active']
        
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    @property
    def skills(self):
        """Parse skills JSON into Python dict"""
        if self.skills_json:
            try:
                return json.loads(self.skills_json)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def set_skills(self, skills_dict):
        """Set skills from Python dict"""
        self.skills_json = json.dumps(skills_dict)
    
    @property
    def is_champion(self):
        """Check if user has champion-level status"""
        return self.role in ['champion', 'elder', 'admin']
    
    @property
    def connection_score(self):
        """Calculate connection potential score"""
        base_score = self.reputation_score
        if self.availability_status == 'available':
            base_score += 10
        if self.dao_participation:
            base_score += 15
        return min(base_score, 100)
    
    def can_connect_with(self, other_user):
        """Check if this user can connect with another user"""
        if self.profile_visibility == 'private':
            return False
        if other_user.profile_visibility == 'private':
            return False
        return True