# route_api_update
update/create routes via .json payload to samsara dashboard. 


Setup:

The main purpose of this program to create a route in the samsara dashboard. 

It’s required to edit the request.json to include vehicle or driver information. Please note that you cannot have both a driverID and a vehicleID, pick one.

The included request.json is a sample route. You may use this example as a way to create your own route. Keep in mind you’ll need to enter your own API token, groupID and driver/vehicle ID for the program to function.


Features:

- Creates a route that includes multiple jobs.
- Edit Lat/Long to any customizable route.

Quick Start on Mac:

1. Install libraries (Matplotlib, JSON, requests through pip or otherwise).
2. Open terminal window. Type “python3 ” then drag the main.py file into the terminal window. Hit enter to start.

For example:
Michaels-MacBook-Pro-4:~ michaelbalzer$ python3 /Users/michaelbalzer/GraphTempProgram/main.py 

Please reference https://www.samsara.com/api for more information
