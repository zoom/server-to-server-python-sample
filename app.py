from flask import Flask, g, Blueprint
from routes.meetings import *
from routes.users import *
from routes.webinars import *
from utils.zoom_token import *

# Create the Flask app
app = Flask(__name__)

# Middleware to set the token and header_config in the global context
@app.before_request
def before_request():
    token = get_token()  
    g.token = token['access_token']
    g.header_config = token['header_config']

# Register the blueprints
app.register_blueprint(meetings_bp)
app.register_blueprint(users_bp)
app.register_blueprint(webinars_bp)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
