#https://github.com/ravisorg/Area-Code-Geolocation-Database/blob/master/us-area-code-geo.csv

from dotenv import load_dotenv
import os
import sys
import csv
import requests

def start_request():
  while True:
    res = input("Proceed with API requests? [Y/n] ").strip().lower()
    if res == "y" or res == "":
      return True
    elif res == "n":
      return False

api_gateway = "https://api.timezonedb.com"
end_point = "/v2.1/get-time-zone"

filename = "us-area-code-geo.csv"
rows = []

load_dotenv()

api_key = os.getenv("API_KEY")
if api_key is None:
  print("No API key found")
  sys.exit(1)


with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  for row in csvreader:
    rows.append(row)
    
print(filename + " successfully loaded")
print("Total number of area codes: %d" % csvreader.line_num)

if start_request() == False:
  sys.exit(0)

##################

params = {
  "key": api_key,
  "format": "json",
  "fields": "abbreviation",
  "by": "position",
  "lat": rows[0][1],
  "lng": rows[0][2]
}



response = requests.get(api_gateway + end_point, params=params)

print(f"Request sent: {response.url}")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print("Response Content:")
    print(response.json())  # Assuming the response is in JSON format
else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Error message: {response.text}")
