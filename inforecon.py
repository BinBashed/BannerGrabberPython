import sys
import requests
import socket
import json

# Banner Grabbing in Python

# We want to print a message to the user if they enter a URL w/ length < 2
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

# Here we make a request to the website provided as an argument on the command line
req = requests.get('https://' + sys.argv[1])
print("\n[HEADER for]: " + sys.argv[0])
print("\n" + str(req.headers))

# Here we've grabbed the host IP of the target and display it nicely to the user
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby_ + "\n")

# Lets now retrieve the latitude and longitude of the target

# We will make an API request to (ipinfo.io) and display it in json format

req2 = requests.get('https://ipinfo.io/' + gethostby_ + "/json")
resp_ = json.loads(req2.text)

print('Location: '+resp_['loc'])
print('Region: '+resp_['region'])
print('City: '+resp_['city'])
print('Country: '+resp_['country'])




