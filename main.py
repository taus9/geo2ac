#https://github.com/ravisorg/Area-Code-Geolocation-Database/blob/master/us-area-code-geo.csv

import csv

filename = "us-area-code-geo.csv"
rows = []

with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  for row in csvreader:
    rows.append(row)
  
  print(filename + " successfully loaded")
  print("Total number of area codes: %d" % csvreader.line_num)
