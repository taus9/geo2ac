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
  
newRows = []
index = 0
while index < len(rows):

  params = {
    "key": api_key,
    "format": "json",
    "fields": "abbreviation",
    "by": "position",
    "lat": rows[index][1],
    "lng": rows[index][2]
  }
  
  response = requests.get(api_gateway + end_point, params=params)  
 
  if response.status_code == 200:
    print(response.json().get("abbreviation"))
    index += 1
  elif response.status_code == 429:
    print("Rate limit retry.")  
  else:
    print("Error skipping code")
    index += 1

