# convertLat3.py
# Purpose: Read a file containing latitudes and convert from
#          decimal-minute-second format to decimal degrees.
# Usage: csv_file_with_latitude_in_second_column
# Example:  C:/gispy/scratch/lats2.csv
import sys

# Get the file path from the user.
theFilePath = sys.argv[1]

# Open the latitude file for reading.
inf = open(theFilePath, 'r')
           
for row in inf:
    ## 1. Get a list containing the three parts.
    rowParts = row.split(',')
    dmsLat = rowParts[1]
    dmsLat = dmsLat.rstrip()
    dmsLatParts = dmsLat.split("-")
            
    ## 2. Set three variables (such as, d, m, and s) to the individual parts of the latitude.
    deg = dmsLatParts[0]
    min = dmsLatParts[1]
    sec = dmsLatParts[2]

    ## 3. Get the numeric portion of  each part.
    deg = deg.replace('d','')
    min = min.replace('m','')
    sec = sec.replace('s','')

    ## 4. Convert the numeric strings to floats
    deg = float(deg)
    min = float(min)
    sec = float(sec)

    ## 5. Calculate decimal degrees
    dd = deg + min/60 + sec/3600

    ## 6. Use 2 variables to print:  The 30d-15m-50s is equivalent to 30.263888889 decimal degrees
    print("The latitude {0} is equivalent to {1:.4f} decimal degrees".format(dmsLat, dd))
          
inf.close()