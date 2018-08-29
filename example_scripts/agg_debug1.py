import arcpy

arcpy.env.workspace = "C:/gispy/scratch"

for numDist in range(100,200,1000):
    # Do Geoprocessing Stuff
    arcpy.env.overwriteOutput = 1
    input = "C:/gispy/data/ch10/park.shp"
    aggreDist = str(numDist), "meter"
    aggreOut = input.split(".")[0] + str(numDist)+ "agg.shp"
    arcpy.AggregatePolygons(input, aggreOut, aggreDist)
    print aggreOut