# smooth_loop_try.py
# This code has a mistake. 
# Step through in the debugger to see how it works.
# Then fix the problem.
import arcpy, sys
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/gispy/data/ch14/"
scratch = "C:/gispy/scratch/"

fc = 'cover.shp'
num = 100
while num <= 500:        
    try:
        output = scratch + f"{fc[:-4]}_smooth{num}.shp"
        tolerance = f"{num} feet"
        arcpy.cartography.SmoothPolygon(fc, output, "PAEK", tolerance)
        print(f"Created: {output}")
    except arcpy.ExecuteError:
        print(arcpy.GetMessages( ))
        x = x + 100
