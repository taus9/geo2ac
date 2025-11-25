#https://github.com/ravisorg/Area-Code-Geolocation-Database/blob/master/us-area-code-geo.csv

from dotenv import load_dotenv
import os
import sys
import csv

load_dotenv()

api_key = os.getenv("API_KEY")
if api_key is None:
  print("No API key found")
  sys.exit(1)

filename = "us-area-code-geo.csv"
rows = []

with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  for row in csvreader:
    rows.append(row)

print(filename + " successfully loaded")
print("Total number of area codes: %d" % csvreader.line_num)
