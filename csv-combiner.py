import sys
import csv
import os

# gets number of comand line arguments
numFiles = len(sys.argv)

# opens writer and sets header
csvwriter = csv.writer(sys.stdout, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
csvwriter.writerow(['email_hash', 'category', 'filename'])

# loop for the number of files
for i in range(1, numFiles):
    # open reader
    with open(sys.argv[i], 'r') as infile:
      csvreader = csv.reader(infile)
      next(csvreader)  # skip first row
      for row in csvreader:
        if row:  # only continue if row is not empty             
            # add 3rd column
            row.append(os.path.basename(sys.argv[i])) # os extracts file name from the file path
            csvwriter.writerow(row)
              