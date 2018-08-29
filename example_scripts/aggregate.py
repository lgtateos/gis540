# aggregate.py

import arcpy

arcpy.env.workspace = "C:/Temp"
arcpy.env.overwriteoutput = True

inputFeatures = "COVER63p.shp" 
aggDistance = "15 Feet" 
outputFeature = "COVER63pAggr.shp"

gp.AggregatePolygons_management(inputFeatures, outputFeature, aggDistance)

