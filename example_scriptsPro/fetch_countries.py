# Purpose: Fetch a file from a url and write the file locally.
import requests
import os

# Set the output directory and url path of the data.
output_dir = "C:/gispy/scratch/"
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

# 1. Download the file
print("Downloading...")
response = requests.get(url)
zip_path = output_dir + "/countries.zip"
with open(zip_path, "wb") as f:
    f.write(response.content)
    print(f"Done! You should now see '{os.path.basename(zip_path)}' in your {output_dir}.")

