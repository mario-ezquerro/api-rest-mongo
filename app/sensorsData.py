"""This module will serve the api request."""

from config import SERVER_IP_PORT
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp


# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')

# Select the database
db = SERVER_IP_PORT.sensorAfarcloudDB

# Select the collection
collection = db.restfulapi



@app.route("/")
def get_initial_response():
    """Welcome message for the API."""
    # Message to the client
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Afarcloud API'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp


@app.route("/api/v1/data", methods=['POST'])
def create_sensor():
    """
       Function to create new data.
    """
    try:
        # Create new data
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))          
        except:
            # Bad request as request body is not available
            # Add message for debugging purpose
            return "", 400

        record_created = collection.insert(body)

        # Prepare the response
        if isinstance(record_created, list):
            # Return list of Id of the newly created item
            return jsonify([str(v) for v in record_created]), 201
        else:
            # Return Id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500


@app.route("/api/v1/data", methods=['GET'])
def fetch_data():
    """
       Function to fetch the data.
    """
    try:
        # Call the function to get the query params
        query_params = helper_module.parse_query_params(request.query_string.decode('UTF-8'))
        # Check if dictionary is not empty
        if query_params:
            # Try to convert the value to int
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}

            # Fetch all the record(s)
            records_fetched = collection.find(query)

            # Check if the records are found
            if records_fetched.count() > 0:
                # Prepare the response
                return dumps(records_fetched)
            else:
                # No records are found
                return "", 404

        # If dictionary is empty
        else:
            # Return all the records as query string parameters are not available
            if collection.find().count > 0:
                # Prepare response if the data are found
                return dumps(collection.find())
            else:
                # Return empty array if no data are found
                return jsonify([])
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500


@app.route("/api/v1/data/<sensor_id>", methods=['POST'])
def update_data(sensor_id):
    """
       Function to update the client.
    """
    try:
        # Get the value which needs to be updated
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as the request body is not available
            # Add message for debugging purpose
            return "", 400

        # Updating the client
        records_updated = collection.update_one({"id": int(sensor_id)}, body)

        # Check if resource is updated
        if records_updated.modified_count > 0:
            # Prepare the response as resource is updated successfully
            return "", 200
        else:
            # Bad request as the resource is not available to update
            # Add message for debugging purpose
            return "", 404
    except:
        # Error while trying to update the resource
        # Add message for debugging purpose
        return "", 500


@app.route("/api/v1/data/<sensor_id>", methods=['DELETE'])
def remove_sensor(sensor_id):
    """
       Function to remove the client.
    """
    try:
        # Delete the client
        delete_sensor = collection.delete_one({"id": int(sensor_id)})

        if delete_sensor.deleted_count > 0 :
            # Prepare the response
            return "", 204
        else:
            # Resource Not found
            return "", 404
    except:
        # Error while trying to delete the resource
        # Add message for debugging purpose
        return "", 500


@app.errorhandler(404)
def page_not_found(e):
    """Send message to the client with notFound 404 status."""
    # Message to the client
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
