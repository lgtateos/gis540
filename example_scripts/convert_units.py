# convert_units.py
# Purpose: Extract coordinates and units to perform a conversion.

coordinate_string = 'X-700000.0,Y-500000.0|UNITS-Foot'

## 1. Split the string into a list of its two main parts using the '|' delimiter.


## 2. Separate the coordinate string from the units string.


## 3. Put the two parts of the coordinate into a list by splitting the coordinate string.


## 4. Index into the coordinates list to set Xstr amd Ystr variables.


## 5. Remove the non-numeric prefixes (e.g., 'X-' and 'Y-') from each coordinate string.


## 6. Convert the cleaned coordinate strings to floats.


## 7. Extract the unit name from the units string.


## 8. Convert the X and Y coordinates from feet to meters (1 meter = 3.28 feet).



## 9. Use an f string and 4 variables to print to print the converted coordinates like this:
## The coordinates (700000.0, 500000.0) in feet are equivalent to (213414.6, 152439.0) in meters.


## For help with the formatting, try the following code.
##import math
##pi = math.pi
##print(pi)
##print(f"Shorten it: {pi:.4f}")