# copy_try.py
# This script is not well designed. 
# Step through in the debugger to see how it works.
# Then rearrange the code to fix the problem.
import arcpy
arcpy.overwriteOutput = True
arcpy.env.workspace = "C:/gispy/data/ch14/"
scratch = "C:/gispy/scratch/"

fcs = arcpy.ListFeatureClasses()
try:
    for fc in fcs:
        scratch_fc = scratch + fc
        arcpy.Copy_management(fc, scratch_fc)
        print( f"******Created: {scratch_fc}******")  
except arcpy.ExecuteError:
    print(arcpy.GetMessages( ))
