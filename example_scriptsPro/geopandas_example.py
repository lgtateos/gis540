# Purpose: Draw a simple map of Africa with geopandas.

import geopandas as gpd
import matplotlib.pyplot as plt

countries = "C:/gispy/scratch/countries/ne_110m_admin_0_countries.shp"
world = gpd.read_file(countries)

# Optional: filter the data, e.g., to focus on a specific continent
africa = world.query('CONTINENT == "Africa"')

# Create a plot
fig, ax = plt.subplots(1, figsize=(10, 6))

# Plot the GeoDataFrame
africa.plot(ax=ax, color='lightblue', edgecolor='black')

# Add a title
ax.set_title("Simple World Map with GeoPandas")

# Display the map
plt.show()