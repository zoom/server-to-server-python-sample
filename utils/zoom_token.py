import base64
import requests
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Access environment variables
ZOOM_CLIENT_ID = os.getenv('ZOOM_CLIENT_ID')
ZOOM_CLIENT_SECRET = os.getenv('ZOOM_CLIENT_SECRET')
ZOOM_ACCOUNT_ID = os.getenv('ZOOM_ACCOUNT_ID')
ZOOM_OAUTH_ENDPOINT = "https://zoom.us/oauth/token"

# Initialize cached token and expiration time variables
cached_token = None
token_expiration = None

def get_token():
    global cached_token, token_expiration

    #  Check if the token is cached and not expired
    if cached_token and token_expiration and token_expiration > time.time():
        return {
            'access_token': cached_token,
            'expires_in': token_expiration - time.time(),
            'header_config': {
                'Authorization': f'Bearer {cached_token}',
                'Content-Type': 'application/json'
            },
            'error': None
        }
    try:
        # Create the authorization header
        auth_string = f"{ZOOM_CLIENT_ID}:{ZOOM_CLIENT_SECRET}"
        encoded_auth = base64.b64encode(auth_string.encode()).decode()

        headers = {
            'Authorization': f'Basic {encoded_auth}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # Prepare the data for the POST request
        data = {
            'grant_type': 'account_credentials',
            'account_id': ZOOM_ACCOUNT_ID
        }
        # Make the POST request
        response = requests.post(ZOOM_OAUTH_ENDPOINT, headers=headers, data=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Parse the JSON response
        result = response.json()
        access_token = result.get('access_token')
        expires_in = result.get('expires_in')

        # Update the cached token and expiration
        cached_token = access_token
        token_expiration = time.time() + expires_in

        header_config = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
    
        return {
            'access_token': access_token, 
            'expires_in': expires_in,
            'header_config': header_config, 
            'error': None}
    except requests.RequestException as error:
        return {
            'access_token': None, 
            'expires_in': None, 
            'error': str(error)}

