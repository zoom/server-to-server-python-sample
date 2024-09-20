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

Open your terminal:

# Clone down this repository
git clone https://github.com/zoom/

# Navigate into the cloned project directory
cd server-to-server-python

# Run pip to install the app dependencies
pip3 install -r requirements.txt

## Config your app

# Create a .env file in the root directory

Create a .env file in the root directory of the project and add the environment variables found in the .env.example file and fill in the values from your Server to Server Oauth app from the Zoom Marketplace.

## Run the app

# Run the app

run python3 app.py

