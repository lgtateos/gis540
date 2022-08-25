# test_setup.py
# Purpose: To check if the sample data is in the correct location.
import arcpy
my_data = "C:/gispy/data/ch02/park.shp"

response = arcpy.Exists(my_data)
if response:
    answer = "YES"
else:
    answer = "NO"

print(f"********* Is the data in the right place? {answer} *********")
