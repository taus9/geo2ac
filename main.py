#https://github.com/ravisorg/Area-Code-Geolocation-Database/blob/master/us-area-code-geo.csv

from dotenv import load_dotenv
import os
import sys
import csv
import requests
import time

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
output = "area-code-time-zone.csv"
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
    newRow = [rows[index][0], response.json().get("abbreviation")]
    newRows.append(newRow)
  elif response.status_code == 429:
    continue
  
  index += 1
  percentage = int((index / len(rows) * 100))
  print(f"{index} of out {len(rows)} - {percentage}%", end="\r")
  
  time.sleep(1) #Rate limit for free accounts is 1 second.


print(f"Requests complete. Saving file...")
with open(output, 'w') as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerows(newRows)
  
  
  
