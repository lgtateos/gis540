# convert_units.py
# Purpose: Extract coordinates and units to perform a conversion.

coordinate_string = 'X-700000.0,Y-500000.0|UNITS-Foot'

## 1. Split the string into a list of its two main parts using the '|' delimiter.
parts = coordinate_string.split("|")

## 2. Separate the coordinate string from the units string.
coord_string = parts[0]
units_string = parts[1]


## 3. Put the two parts of the coordinate into a list by splitting the coordinate string.
coor_parts =  coord_string.split(",")

## 4. Index into the coordinates list to set Xstr amd Ystr variables.

Xpart = coor_parts[0]
Ypart = coor_parts[1]

## 5. Remove the non-numeric prefixes (e.g., 'X-' and 'Y-') from each coordinate string.
Xstr = Xpart.strip("X-")
Ystr = Ypart.strip("Y-")

## 6. Convert the cleaned coordinate strings to floats.
X = float(Xstr)
Y = float(Ystr)

## 7. Extract the unit name from the units string.

unit = units_string.replace("UNITS-","")

## 8. Convert the X and Y coordinates from feet to meters (1 meter = 3.28 feet).

Xmeters = X/3.28
Ymeters = Y/3.28

## 9. Use an f string and 4 variables to print to print the converted coordinates like this:
## The coordinates (700000.0, 500000.0) in feet are equivalent to (213414.6, 152439.0) in meters.
message = f"The coordinates ({X:.1f}, {Y:.1f}) in feet are equivalent to ({Xmeters:.1f}, {Ymeters:.1f}) in meters."
print(message)


## For help with the formatting, try the following code.
##import math
##pi = math.pi
##print(pi)
##print(f"Shorten it: {pi:.4f}")


## Addional notes:

## You could combine some of these steps by chaining them together.  For example
## this code combines three steps into one line of code:
## X = float(coor_parts[0].replace("X-", ""))

## However, this is not recommended for beginners.  For two reasons:
## 1) This the code more difficult to understand
## 2) It makes DEBUGGING more difficult!