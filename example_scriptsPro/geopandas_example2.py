# Purpose: Draw an African population graduated color map with geopandas.
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Load and Filter
countries_path = "C:/gispy/scratch/natural_earth_data/ne_110m_admin_0_countries.shp"
world = gpd.read_file(countries_path)
africa = world.query('CONTINENT == "Africa"').copy() # .copy() prevents 'SettingWithCopy' warnings

# 2. DATA TRANSFORMATION: Convert to Millions for readability
africa['POP_MILLIONS'] = africa['POP_EST'] / 1_000_000

# 3. Create the plot
fig, ax = plt.subplots(1, figsize=(12, 8))

# 4. Plot with graduated colors
# We use 'POP_MILLIONS' so the numbers in the legend are smaller (e.g., 200 instead of 200,000,000)
plot = africa.plot(column='POP_MILLIONS', 
                   ax=ax, 
                   cmap='YlOrRd', 
                   legend=True, 
                   edgecolor='black',
                   linewidth=0.4,
                   legend_kwds={'label': "Population (Millions)", 
                                'orientation': "horizontal",
                                'pad': 0.05})

# 5. LEGEND FORMATTING: Force standard numbers (no scientific notation)
# This finds the colorbar axis and applies a plain scalar formatter
colorbar = ax.get_figure().get_axes()[-1]
colorbar.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))

# Clean up
ax.set_title("African Population by Country", fontsize=16)
ax.axis('off')

plt.show()