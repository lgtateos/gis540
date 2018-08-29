#buffer_clip.py (hard-coded version)
#Purpose: Buffer a zone and use it to clip another file

import arcpy, sys 

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/Temp/"

# Set buffer params
fireDamage = "special_regions.shp"
fireBuffer = fireDamage[:-4] + "_buffer.shp"
bufferDist = "1 mile"

# Set clip params 
park = "COVER63p.shp" 
clipOutput = park[:-4] + "_damageBuffer.shp"

arcpy.Buffer_analysis(fireDamage, fireBuffer,bufferDist) 
arcpy.Clip_analysis(park, fireBuffer, clipOutput )