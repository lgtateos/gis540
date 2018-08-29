import arcpy
#Create a map layer object. Cover63p3.lyr must be a file already.
addLayer = arcpy.mapping.Layer("C:/Temp/Cover63p3.lyr") 

mapName = "C:/Temp/test.mxd"
mxd = arcpy.mapping.MapDocument(mapName)
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0] #get the first data frame
arcpy.mapping.AddLayer(df, addLayer)
copyName = mapName[:-4] + "2.mxd"
mxd.saveACopy(copyName)