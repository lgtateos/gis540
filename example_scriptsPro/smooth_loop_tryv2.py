# smooth_loop_tryv2.py

import arcpy
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
    num = num + 100
