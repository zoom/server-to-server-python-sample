# Zoom API Server to Server OAuth Starter App Python
This sample application serves as a boilerplate Flask app for interacting with the Zoom API. It implements the Server-to-Server OAuth flow to generate access tokens and make authorized API calls to Zoom.

The use of this sample app is subject to our Terms of Use
https://marketplace.zoom.us/docs/api-reference/terms-of-use


## Prerequisites
To use this app, ensure you have the following:
- Python 3.8+
- Flaskk 2.0+
- Server to Server Oauth app
- Zoom API Account Admin privileges

## Key features
**Server-to-Server OAuth:** Easily authenticate your application and securely generate access tokens.
**Flask Framework:** Built with Flask, this app provides a lightweight and efficient way to handle web requests.

## Getting Started

### Create a Server-to-Server OAuth app
1. Create a server-to-server OAuth app: Before cloning the repository, set up your app and get your credentials. For questions on this, reference the docs on creating a server-to-server app. Make sure you activate the app. Follow our [set up documentation](https://developers.zoom.us/docs/internal-apps/) or this [video](https://www.youtube.com/watch?v=OkBE7CHVzho) for a more complete walk through.

2. Add scopes to your app. 
Under the meeting section, add the following scopes:
- meeting:write:meeting:admin 
- meeting:read:meeting:admin 
- meeting:update:meeting:admin
- meeting:delete:meeting:admin  
- meeting:read:list_past_participants:admin

Under the webinar section, add the following scopes:
- webinar:read:webinar:admin
- webinar:write:webinar:admin
- webinar:update:webinar:admin
- webinar:delete:webinar:admin
- webinar:read:list_panelists:admin

Under the user section, add the following scopes:
- user:read:list_users:admin
- user:read:user:admin
- user:write:user:admin
- user:read:settings:admin
- user:update:settings:admin


Note: If you add additional API routes to this starter app, you may need to add the corresponding scopes. You can find a list of the available granular scopes in our [API reference](https://developers.zoom.us/docs/integrations/oauth-scopes-granular/).

### Clone this repository
Open your terminal and run the following command:
`$ git clone https://github.com/zoom/`

### Setup
1. In terminal, navigate into repository:
`$ cd server-to-server-python`

2. Install the app dependencies: 
`$ pip3 install -r requirements.txt`

3. Create a .env file in the root directory. Copy the values from the .env.example file and fill in your Server-to-Server OAuth app credentials from the Zoom Marketplace:
`touch .env`

4. Run the app:
`python3 app.py`

### Usage
Once the app is running, it wlll be available to test at http://127.0.0.1:5000, and you will be able to make requests to the Zoom APIs.

To test, open up a terminal or a tool like Postman or Insomnia and send a GET request to http://127.0.0.1:5000/users. If everything's set up correctly, this will return a list of all the users on your account.

Your server now provides the following API Routes:

**Meeting Routes**
- GET /meetings/:meeting_id
- POST /users/:user_id/meetings
- PATCH /meetings/:meeting_id
- DELETE /meeting/:meeting_id
- GET /meetings/:meeting_id/participants

**Webinar Routes**
- GET /webinars/:webinar_id
- POST /users/:user_id/webinars
- PATCH /webinars/:webinar_id
- DELETE /webinars/:webinar_id
- GET /webinars/:webinar_id/panelists

**User Routes**
- GET /users
- GET /users/:user_id
- POST /users
- GET /users/:user_id/settings
- PATCH /users/:user_id/settings

### Add new routes
To add new routes, create a new file in the routes directory, load and access environment variables, and create a Blueprint for the new routes before defining them. Finally, import all the routes into your app.py file and register with the Blueprint.