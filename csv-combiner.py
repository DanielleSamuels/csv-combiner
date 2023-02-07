import sys
import csv
import os

# sys.argv
numFiles = len(sys.argv)
# for i in range(1, numFiles):
  #  print(sys.argv[i], end = " ")

outputFile = "out.csv"

with open(sys.argv[1], 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)    # skip first row
  for row in csvreader:
    if row:  # only continue if row is not empty             
        newRow = row
        newRow.append(os.path.basename(sys.argv[1]).split('/')[-1]) # os extracts file name from the file path
        print(newRow)
