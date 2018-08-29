#Purpose: Convert shapes to points 
#         by calling a tool found on online
#         at ESRI scripts
#Author: Laura Tateosian
#Date: July 21, 2008
import arcgisscripting, os
gp = arcgisscripting.create()

gp.overwriteoutput = 1
gp.workspace = "C:/Temp/"
gp.addToolbox("C:/Temp/shapeToPoints/ShapesToPoints.tbx")
gp.ShapesToPnts_s2p("COVER63p.shp", "true", "COVER63p_points1.txt","#","COVER63p_points1.shp" )