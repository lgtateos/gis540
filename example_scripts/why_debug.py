#Name: basin_process_tool.py
#
#Description: written to process 10 and 12 digit HUCs for the DWQ project
#
#Requirements: Be cool, man.  Be cool.

# Import system modules
import sys, string, os

#input directory with KML files
InKMLSpace = "C:\\temp"

#set directory with corresponding geospacial information (spapefiles or feature classes...)
GeoDirectory = "C:\\temp"

#Get a list of files in the InKMLSpace
FileList = os.listdir(InKMLSpace)

for file in FileList:

    if file.endswith("kml"):
        #open KML document
        #set variables for conditional statement that checks geospatial file type
        shapefile = GeoDirectory + "\\" + file[:-4] + ".shp"
        featureClass = GeoDirectory + "\\" + file[:-4]

        #check to see if corresponding geospatial file is a shapefile or a feature class
        if os.path.exists(shapefile):
            featurerLayer = shapefile
            print "shapefile"
        elif os.path.exists(featureClass):
            featureLayer = featureClass
            print "feature class"
        else:
            featureLayer = "no matching files."

        print featureLayer

    else:
        print file + " is not a KML file, skipping."