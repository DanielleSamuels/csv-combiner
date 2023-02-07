import sys
import csv
import os

# gets number of comand line arguments
numFiles = len(sys.argv)

# FOR TESTING - REMOVE LATER
outputFile = "out.csv"

# opens writer and sets header
with open(outputFile, 'w', newline='') as outfile:
  csvwriter = csv.writer(outfile, delimiter=',')
  csvwriter.writerow(['email_hash', 'category', 'filename'])
  # loop for the number of files
  for i in range(1, numFiles):
    # open reader
    with open(sys.argv[i], 'r') as infile:
      csvreader = csv.reader(infile)
      next(csvreader)    # skip first row
      for row in csvreader:
        if row:  # only continue if row is not empty             
            # add 3rd column
            newRow = row
            newRow.append(os.path.basename(sys.argv[1]).split('/')[-1]) # os extracts file name from the file path
            csvwriter.writerow(newRow)
