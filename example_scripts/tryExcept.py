import arcpy, sys
arcpy.env.overwriteOutput = 1
arcpy.env.workspace = "C:/Temp"
try:
    file = sys.argv[1]
    print "HURRAY"
    outfile = sys.argv[2]
    print "WOOPEEE!"
    distance = sys.argv[3]
    print "FAB"
except:
    print "DOOFUS"
    if len(sys.argv) == 1: #no arguments given
        file = "COVER63p.shp"
        outfile = "outputBuffer.shp"
        distance = "1 mile"
        print "PHEW"
    elif len(sys.argv) == 2:  #one argument was given
        outfile = "outputBuffer.shp"
        distance = "1 mile"
        print "AT LAST"
    else: # two arguments given
        distance = "1 mile"
        print "ROGER"
      
outputFile = arcpy.Buffer_analysis(file,outfile, distance)
print "SHAZAM"


#Predict what will be printed with these inputs:
#-----------------------------------------------------

#1. no arguments

#2. NEROFires.shp

#3. NEROFires.shp "buff.shp"

#4. NEROFires.shp "buff.shp" "2 miles"

#5. test.txt "buff.shp" "2 miles"