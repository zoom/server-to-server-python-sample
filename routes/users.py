from flask import Flask, jsonify, request, Blueprint
import requests
from dotenv import load_dotenv
import os

#  Load and access environment variables from .env
load_dotenv()     
ZOOM_API_BASE_URL = os.getenv('ZOOM_API_BASE_URL')

# Create a Blueprint for the meetings routes
users_bp = Blueprint('users', __name__)

# Define the routes

# List users
# https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/users
@users_bp.route('/users', methods=['GET'])
def get_users():
    token_result = get_token()
    access_token = token_result['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(f"{ZOOM_API_BASE_URL}/users", headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': "Error getting users"
        }), 500

# Get a user
# https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/user
@users_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    token_result = get_token()
    access_token = token_result['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(f"{ZOOM_API_BASE_URL}/users/{user_id}", headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error getting user with ID: {user_id}"
        }), 500


# Create a user
# https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userCreate
@users_bp.route('/users', methods=['POST'])
def post_user():
    token_result = get_token()
    access_token = token_result['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    body = request.json

    try:
        response = requests.post(f"{ZOOM_API_BASE_URL}/users", json=body, headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': "Error creating user"
        }), 500


# Get user settings
# https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSettings
@users_bp.route('/users/<user_id>/settings', methods=['GET'])
def get_user_settings(user_id):
    token_result = get_token()
    access_token = token_result['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(f"{ZOOM_API_BASE_URL}/users/{user_id}/settings", headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error getting user settings for user with ID: {user_id}"
        }), 500

# Update user settings
# https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userSettingsUpdate
@users_bp.route('/users/<user_id>/settings', methods=['PATCH'])
def patch_user_settings(user_id):
    token_result = get_token()
    access_token = token_result['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    body = request.json

    try:
        response = requests.patch(f"{ZOOM_API_BASE_URL}/users/{user_id}/settings", json=body, headers=headers)
        response.raise_for_status()
        #data = response.json()
        return str(response.status_code), response.status_code
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error updating user settings for user with ID: {user_id}"
        }), 500