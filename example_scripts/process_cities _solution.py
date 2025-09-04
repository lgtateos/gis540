# process_cities.py
# Purpose: Convert a CSV of cities into a shapefile and project it.
# Usage: data_directory output_directory basename_of_cities_file
# Example: C:/gispy/data/ch06 C:/gispy/scratch africa_cities.csv

## Step 1: Set up the environment.
import arcpy
import os
import sys

# Set the workspace to the data directory given by the user.
arcpy.env.workspace = sys.argv[1]


# Define a variable for the output directory given by the user
# which will be used for temporary and final outputs.
scratch_dir = sys.argv[2]
if not os.path.exists(scratch_dir):
    os.makedirs(scratch_dir)

# Allow existing outputs to be overwritten.
arcpy.env.overwriteOutput = True

# Create a variable set to the input CSV file name given by the user.
in_csv_name = sys.argv[3]

## Step 2: Make a copy of the input file.
out_csv_path = os.path.join(scratch_dir, in_csv_name)
arcpy.management.Copy(in_csv_name, out_csv_path)

# Change the workspace to the output directory for the next steps.
arcpy.env.workspace = scratch_dir

## Step 3: Create a Point Shapefile.
# Get the base name of the file without the extension.
shp_name_base = os.path.splitext(in_csv_name)[0]
# Use basename + ".shp" to make a shapefile name.
out_shp_name = shp_name_base + ".shp"

# Call the Make XY Event Layer (Data Management) tool to
# create a temporary point layer from the CSV.
# The data has 'longitude' and 'latitude' fields.
temp_layer = arcpy.management.MakeXYEventLayer(out_csv_path, "longitude", "latitude", "cities_layer")

# Call the Copy Features (Data Management) tool to
# save the temporary layer as a permanent shapefile.
arcpy.management.CopyFeatures(temp_layer, out_shp_name)

## Step 4: Add a new field.
# Create a new name for the projected shapefile in the same directory.
# (using the output base name variable you already created + "_projected.shp"
arcpy.management.AddField(out_shp_name, "hemisphere", "TEXT")

## Step 5: Project the data.
# Create a new name for the projected shapefile in the same directory.
projected_shp_name = shp_name_base + "_projected.shp"
out_projected_path = os.path.join(scratch_dir, projected_shp_name)

# Project the shapefile to the World from Space projection (EPSG 102038).
arcpy.management.Project(out_shp_name, out_projected_path, 102038)

## Step 6: Print using the projected file name variable to confirm completion.
print(f"The projected shapefile has been successfully created at: {out_projected_path}")