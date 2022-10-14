# copy_tryv2.py
import arcpy
arcpy.overwriteOutput = True
arcpy.env.workspace = "C:/gispy/data/ch14/"
scratch = "C:/gispy/scratch/"

fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    try:
        scratch_fc = scratch + fc
        arcpy.Copy_management(fc, scratch_fc)
        print( f"******Created: {scratch_fc}")  
    except arcpy.ExecuteError:
        print(arcpy.GetMessages())
