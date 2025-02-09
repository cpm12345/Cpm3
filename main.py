import requests
from time import sleep

BASE_URL = "https://cpmelsedevshop.squareweb.app/api"

class CPMElsedev:
    def __init__(self, access_key):
        self.auth_token = None
        self.access_key = access_key

    def login(self, email, password):
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        try:
            response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            response_decoded = response.json()
            if response_decoded.get("ok"):
                self.auth_token = response_decoded.get("auth")
            return response_decoded.get("error")
        except requests.exceptions.RequestException as e:
            print(f"Error during login: {e}")
            return None
    
    # Define other methods like register(), delete(), etc. in similar fashion

    def set_player_money(self, amount):
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        try:
            response = requests.post(f"{BASE_URL}/set_money", params=params, data=payload)
            response.raise_for_status()
            response_decoded = response.json()
            return response_decoded.get("ok")
        except requests.exceptions.RequestException as e:
            print(f"Error setting player money: {e}")
            return False

    # You can repeat similar patterns for other API calls...
  
