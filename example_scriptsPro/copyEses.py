# copyEses.py
# Copy feature classes from gdb to a new gdb.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch11/tester.gdb'
fcs = arcpy.ListFeatureClasses('s*','POINT')  #Step 1
res = arcpy.CreateFileGDB_management('C:/gispy/scratch', 'out.gdb')  #Step 2
destWorkspace = res.getOutput(0)

for fc in fcs: 
    # Create output name with destination path
    destination = destWorkspace + '/' + fc
    # Copy the features to C:/gispy/scratch/out.gdb
    arcpy.management.Copy(fc, destination)   #Step 3 