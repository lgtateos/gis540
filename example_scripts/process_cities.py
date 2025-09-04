# process_cities.py
# Purpose: Convert a CSV of African cities into a shapefile and project it.
# Usage: data_directory output_directory basename_of_cities_file
# Example input: C:/gispy/data/ch06 C:/gispy/scratch africa_cities.csv

## Step 1: Set up the environment.
# import the modules you need


# Set the workspace to the data directory given by the user.


# Create a variable set to the output directory given by the user
# which will be used for temporary and final outputs.


# Allow existing outputs to be overwritten.

# Create a variable set to the input CSV file name given by the user.


## Step 2: Make a copy of the input file.
# Use os.path.join to set a variable to the full path name of the output.

# Make a copy of the input file in the output directory.
# Use the arcpy Copy (data management) tool to make the copy.


# Change the workspace to the output directory for the next steps.


## Step 3: Create a Point Shapefile.

# Call the Make XY Event Layer (Data Management) tool to
# create a temporary point layer from the CSV.
# The data has 'longitude' and 'latitude' fields.

# Get the base name of the file without the extension.

# Use basename + ".shp" to make a variable holding the output shapefile name.


# Call the Copy Features (Data Management) tool to
# save the temporary layer as a permanent shapefile.


## Step 4: Add a new field.
# Add a text field named 'hemisphere' to the newly created shapefile.


## Step 5: Project the data.
# Create a new name for the projected shapefile in the same directory.
# (using the output base name variable you already created + "_projected.shp"


# Project the shapefile to the World from Space projection (EPSG 102038).


## Step 6: Print using the projected file name variable to confirm completion.
# For example:
# The projected shapefile has been successfully created at: C:/gispy/scratch/africa_cities_projected.shp
