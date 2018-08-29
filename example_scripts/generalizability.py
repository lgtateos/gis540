#############################################################################################################################
#Script Explanation:
#This procedure takes a shapefile that has an attribute table of x, y coordinates followed by the names of DEM years.
#This shapefile contains elevations extracted from each raster at each x,y coordinate. Under each DEM year (field name) are
#a list of elevations in meters associated with each x,y point. This script uses a procedure with dictionaries to store keys
#(field names: DEM names) and values (extracted elevations in meters). Shortly I'll be able to subtract 1998 LiDAR (which we
#are assume is our elevation for comparison) to fix the vertical shifts then I'll calculate the median values to subtract or
#add to the 1998 and 2001 data set since we know these two data sets are in fact shifted. Other DEMs will not be shifted due
#to them being within the published accuracy of the LiDAR data set or we have little information from the others to be able
#to confidently shift the data sets. d[f] is a dictionary that contains items (field names: values)
#############################################################################################################################

def PullOutTimeSeriesXYZ( extracted_values_shape ):
        fields=arcpy.ListFields(extracted_values_shape)
        FieldsList=[]
        d={}
        for field in fields:
            field_name=field.name
            if field_name !="FID" and field_name !="Shape":
                FieldsList.append( field_name )
        for f in FieldsList:
            sc=arcpy.SearchCursor(extracted_values_shape)
            for line in sc:
                value=line.getValue(f)
                if d.has_key(f):
                    d[f].append(value)
                else:
                    d[f]=[value]
        return d

dict = PullOutTimeSeriesXYZ("C:/Temp/COVER63p.shp")
print dict
                    