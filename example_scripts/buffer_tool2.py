import arcpy

distance = "5 Feet" # provide a default value if unspecified
arcpy.env.overwriteOutput = 1

input = "C:/Temp/COVER63p.shp" # provide a default value if unspecified

# Local variables...
output = "C:/Temp/COVER63p_Buffer.shp"

# Process: Buffer...
arcpy.Buffer_analysis(input, output, distance, "FULL", "ROUND", "NONE", "")




