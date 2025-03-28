import requests
import json
import os
from typing import Dict, Any, Optional

class APIClient:
    def __init__(self):
        # API Ayarları - TEST AMAÇLIDIR
        self.base_url = "https://api.example.com"
        self.api_key = "sk_live_51ABcDeFGhIjkLMno0123456789abcdefghijklmnopqrstuvwxyz"
        self.github_token = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789"
        
        # Kullanıcı kimlik bilgileri
        self.credentials = {
            "username": "admin@example.com",
            "password": "Admin_123!"
        }
        
        # JWT token örneği
        self.jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlRlc3QgVXNlciIsImlhdCI6MTUxNjIzOTAyMn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

    def get_headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.jwt_token}",
            "X-API-Key": self.api_key
        }
    
    def get_users(self) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/users"
        response = requests.get(endpoint, headers=self.get_headers())
        return response.json()
    
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/users"
        response = requests.post(endpoint, headers=self.get_headers(), json=user_data)
        return response.json()
    
    def connect_to_database(self):
        # DB bağlantı bilgileri - TEST AMAÇLIDIR
        db_config = {
            "host": "db.example.com",
            "port": 3306,
            "username": "dbuser",
            "password": "DB_password_123!",
            "database": "testproject"
        }
        
        connection_string = f"mysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        return connection_string

# Kullanım örneği
if __name__ == "__main__":
    client = APIClient()
    users = client.get_users()
    print(json.dumps(users, indent=2))
