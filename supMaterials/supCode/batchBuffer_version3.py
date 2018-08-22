# batchBuffer_version3.py
# Purpose: Buffer each file in the given workspace by the given number
#          of miles and put the results in an output workspace.
# Usage: data workspace, number of miles
import arcpy, os, sys
arcpy.env.workspace = sys.argv[1]
outputDir = arcpy.env.workspace + '/results'
distance = 'str(sys.argv[2]) miles'
if not os.path.exists( outputDir ):
	os.mkdir( outputDir )

fcs = arcpy.ListFeatureClasses( ) 
for fc in fcs:
	# SET the output variable 
	fcBuffer = outputDir + fc[:-4] + '_buffer.shp'
	# CALL buffer tool
	arcpy.Buffer_analysis(fc, fcBuffer, distance)
	print 'Buffer output {0} created in {1}'.format(fcBuffer, outputDir)