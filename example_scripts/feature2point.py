import arcpy, sys, os

#Set up variables
arcpy.env.overwriteOutput = True
inputfile = sys.argv[1]
outputfile = os.path.dirname(inputfile) + "/" + "outPoints.shp"

#Find a point based on the input
arcpy.FeatureToPoint_management(inputfile, outputfile)

##Set the output parameter


