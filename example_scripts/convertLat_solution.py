# convertLat.py
# Purpose: Convert 30 degrees 15 minutes and 50 seconds angle to decimal degrees.
# Conversion formula:
#           decimalDegrees = degrees + minutes/60 + seconds/3600

lat = "30d-15m-50s" #(Assume this is for latitude North)

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