from flask import Flask, g, jsonify, request, Blueprint
import requests
from dotenv import load_dotenv
import os

#  Load and access environment variables from .env
load_dotenv()     
ZOOM_API_BASE_URL = "https://api.zoom.us/v2"

# Create a Blueprint for the meetings routes
meetings_bp = Blueprint('meetings', __name__)

# Define the routes

# Get a meeting
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meeting
@meetings_bp.route('/meetings/<meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    headers=g.header_config
    try:
        response = requests.get(f"{ZOOM_API_BASE_URL}/meetings/{meeting_id}", headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error getting meeting with ID: {meeting_id}"
        }), 500


# Create a meeting
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingCreate
@meetings_bp.route('/users/<user_id>/meetings', methods=['POST'])
def post_meeting(user_id):
    headers=g.header_config
    try:
        response = requests.post(f"{ZOOM_API_BASE_URL}/users/{user_id}/meetings", json=request.json, headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error creating meeting for {user_id}"
        }), 500

# Update a meeting
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingUpdate  
@meetings_bp.route('/meetings/<meeting_id>', methods=['PATCH'])
def patch_meeting(meeting_id):
    headers=g.header_config
    try:
        response = requests.patch(f"{ZOOM_API_BASE_URL}/meetings/{meeting_id}", json=request.json, headers=headers)
        response.raise_for_status()
        #data = response.json()
        return str(response.status_code), response.status_code
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error updating meeting with ID: {meeting_id}"
        }), 500

# Delete a meeting
# https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingDelete  
@meetings_bp.route('/meetings/<meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    headers=g.header_config
    try:
        response = requests.delete(f"{ZOOM_API_BASE_URL}/meetings/{meeting_id}", headers=headers)
        response.raise_for_status()
        return str(response.status_code), response.status_code
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error deleting meeting with ID: {meeting_id}"
        }), 500

# Get past meeting participants
#https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/pastMeetingParticipants
@meetings_bp.route('/past_meetings/<meeting_id>/participants', methods=['GET'])
def get_meeting_participants(meeting_id):
    headers=g.header_config
    try:
        response = requests.get(f"{ZOOM_API_BASE_URL}/past_meetings/{meeting_id}/participants", headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as err:
        return jsonify({
            'error': str(err),
            'message': f"Error getting participants for meeting with ID: {meeting_id}"
        }), 500



