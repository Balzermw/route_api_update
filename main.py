import time

# Importing our modules
from settings import Constants
from route_creator import RouteCreator

# Entry Point
def main():
    # Route Creator Object (Deals with API and reads/writes request/response files)
    route_creator = RouteCreator(Constants.request_body_file, Constants.response_body_file)
    
    # Creates the routes as defined in the request_body_file json file
    route_creator.create()

# If the file is being executed as main file (i.e: not being used as a module)
if __name__ == "__main__":
    main()