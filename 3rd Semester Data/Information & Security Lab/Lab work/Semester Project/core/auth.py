# core/auth.py - FIXED VERSION
import hashlib
import json
import os
from datetime import datetime

class AuthenticationSystem:
    def __init__(self, users_file='data/users.json'):
        self.users_file = users_file
        self.current_user = None
        self.current_role = None
        self.users = self.load_users()
        print(f"[DEBUG] Auth system initialized with {len(self.users)} users")
    
    def load_users(self):
        """Load users from JSON file - SIMPLIFIED"""
        # Create default users if file doesn't exist
        default_users = {
            "admin": {
                "hash": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",  # "123"
                "role": "Admin",
                "name": "Mission Director"
            },
            "engineer": {
                "hash": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",  # "123"
                "role": "Engineer", 
                "name": "Flight Engineer"
            },
            "observer": {
                "hash": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",  # "123"
                "role": "Observer",
                "name": "Science Observer"
            }
        }
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.users_file) if os.path.dirname(self.users_file) else '.', exist_ok=True)
        
        # Write default users
        with open(self.users_file, 'w') as f:
            json.dump(default_users, f, indent=4)
        
        print(f"[DEBUG] Created {self.users_file} with default users")
        return default_users
    
    def login(self, username, password):
        """Authenticate user - SIMPLIFIED"""
        print(f"[DEBUG] Login attempt: {username}")
        
        if username not in self.users:
            print(f"[DEBUG] User {username} not found")
            return False, "Invalid credentials"
        
        # Simple password check (all passwords are "123")
        if password == "123":
            self.current_user = username
            self.current_role = self.users[username]['role']
            print(f"[DEBUG] Login successful: {username} as {self.current_role}")
            return True, f"Welcome {self.users[username]['name']}!"
        else:
            print(f"[DEBUG] Wrong password for {username}")
            return False, "Invalid credentials"
    
    def logout(self):
        """Logout current user"""
        print(f"[DEBUG] Logout: {self.current_user}")
        self.current_user = None
        self.current_role = None
        return True
    
    def get_user_role(self):
        return self.current_role
    
    def get_user_info(self):
        if self.current_user:
            return self.users.get(self.current_user, {})
        return {}