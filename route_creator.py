import json
import requests

from datetime import datetime

from settings import Constants

class RouteCreator():

    # Constructor
    def __init__(self, body_file, response_file):
        self.body_file = body_file  # The filename from which the request body will be loaded
        self.response_file = response_file  # The filename at which the response json will be stored

    def create(self):
        # POST Request's Body
        with open(self.body_file, "r") as file:
            body = json.loads(file.read())

        # Request's Query Parameter (appended to URL after ?)
        params = {
            "access_token": Constants.access_token
        }

        # Sending a POST request to the create route endpoint
        response = requests.post(Constants.route_api_endpoint, params=params, json=body)

        # If response status code is not 200 OK, something is wrong, so raise exception
        if response.status_code != 200:
            raise Exception("Non OK Response from Server. Response:\n" + response.text)
        
        # Parse response as json (to dictionary)
        response = response.json()

        # Save response to a file
        with open(self.response_file, "w") as file:
            # Write pretty-printed json to the response file
            file.write(json.dumps(response, indent=4))
        
        print(F"Successfully saved response to {self.response_file}.")