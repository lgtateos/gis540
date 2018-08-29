import arcpy, sys

tableName = sys.argv[1] # Or use arcpy.GetParameterAsText(0)
fieldName = sys.argv[2] # Or use arcpy.GetParameterAsText(1)

print "Checking table:", tableName
print "For fieldname", fieldName

# Using two arguments( InputValue, wildCard ) so that the
# numerator will either return 1 or 0 fields. Since no "*" is used,
# at most one field will exactly match the wildcard.
fields = arcpy.ListFields(tableName)

fieldNames = [field.name for field in fields]

if fieldName in fieldNames: # if the fieldName is already a field in the table, set exists to true and does_not_exist to false
        print "Field", fieldName, "found in", tableName
        arcpy.AddMessage("Field " + fieldName + " found in " + tableName)
        arcpy.SetParameterAsText(2, "True") # Sets the 3rd parameter, Exists, to true (0-based)
        arcpy.SetParameterAsText(3, "False") # Sets the 4th parameter, Does_Not_Exist, to false (0-based)



else: # else the fieldName is not yet a field in the table,so set exists to false and does_not_exist to true
        print"Field", fieldName, "NOT found in", tableName
        arcpy.AddMessage("Field " + fieldName + " NOT found in " + tableName)
        arcpy.SetParameterAsText(2, "False") # Sets the 3rd parameter, Exists, to false
        arcpy.SetParameterAsText(3, "True") # Sets the 4th parameter, Does_Not_Exist, to true

raw_input("Click ENTER to close the window")

