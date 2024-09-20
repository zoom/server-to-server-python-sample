S2S OAuth Starter App

The use of this sample app is subject to our Terms of Use
https://marketplace.zoom.us/docs/api-reference/terms-of-use

# Zoom API Server to Server OAuth Starter App
This app is a boilerplate flask app to call the Zoom API.
It uses a Server to Server Oauth flow to generate an access token and call the Zoom API.

Built with Flask and Zoom API. 

## Prerequisites

- Python 3.8+
- Flaskk 2.0+
- Server to Server Oauth app
- Zoom API Account Admin privileges


## Getting Started

### Clone down this repository
Open your terminal and run the following commands:

`$ git clone https://github.com/zoom/`

### Setup
1. In terminal, cd into the cloned repository
`$ cd server-to-server-python`

2. Install the app dependencies
`$ pip3 install -r requirements.txt`

3. Create a .env file in the root directory and copy the values from the .env.example file and fill in the values from your Server to Server Oauth app from the Zoom Marketplace.
`touch .env`

4. Run the app

`python3 app.py`

