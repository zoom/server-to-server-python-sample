from flask import Flask, g, jsonify, request, Blueprint
import requests
from dotenv import load_dotenv
import os

#  Load and access environment variables from .env
load_dotenv()     
ZOOM_API_BASE_URL = os.getenv('ZOOM_API_BASE_URL')

# Create a Blueprint for the webinars routes
webinars_bp = Blueprint('webinars', __name__)

# Define the routes

# Get a webinar
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinar
@webinars_bp.route('/webinars/<webinar_id>', methods=['GET'])
def get_webinar(webinar_id):
    headers=g.header_config
    try:
        response = requests.get(f"{ZOOM_API_BASE_URL}/webinars/{webinar_id}", headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error getting webinar with ID: {webinar_id}"
        }), 500

# Create a webinar 
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarCreate
@webinars_bp.route('/users/<user_id>/webinars', methods=['POST'])   
def post_webinar(user_id):
    headers=g.header_config
    try:
        response = requests.post(f"{ZOOM_API_BASE_URL}/users/user_id/webinars", json=request.json, headers=headers)     
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error creating webinar for {user_id}"
        }), 500

# Update a webinar
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarUpdate
@webinars_bp.route('/webinars/<webinar_id>', methods=['PATCH'])
def patch_webinar(webinar_id):
    headers=g.header_config
    try:
        response = requests.patch(f"{ZOOM_API_BASE_URL}/webinars/{webinar_id}", json=request.json, headers=headers)
        response.raise_for_status()
        return str(response.status_code), response.status_code
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error updating webinar with ID: {webinar_id}"
        }), 500

# Delete a webinar
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarDelete
@webinars_bp.route('/webinars/<webinar_id>', methods=['DELETE'])
def delete_webinar(webinar_id):
    headers=g.header_config
    try:
        response = requests.delete(f"{ZOOM_API_BASE_URL}/webinars/{webinar_id}", headers=headers)   
        response.raise_for_status()
        return str(response.status_code), response.status_code
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error deleting webinar with ID: {webinar_id}"
        }), 500

# List webinar panelists
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarPanelists
@webinars_bp.route('/webinars/<webinar_id>/panelists', methods=['GET'])
def get_webinar_panelists(webinar_id):
    headers=g.header_config
    try:
        response = requests.get(f"{ZOOM_API_BASE_URL}/webinars/{webinar_id}/panelists", headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error getting webinar panelists for webinar with ID: {webinar_id}"
        }), 500