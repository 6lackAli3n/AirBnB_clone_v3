#!/usr/bin/python3
"""
This module contains the main Flask application instance.
It sets up the application and registers the necessary
blueprints and handlers.
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors that returns a
    JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
