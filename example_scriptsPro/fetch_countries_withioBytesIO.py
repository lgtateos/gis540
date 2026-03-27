##import requests
##import zipfile
##import io
##import os
##
##url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
##
##response = requests.get(url)
##if response.status_code == 200:
## 	with open("countries.zip", "wb") as f:
## 	 	f.write(response.content)
## 	 	print(data)
##
##print(response.status_code)


import requests
import zipfile
import io
import os

os.chdir("C:/gispy/scratch/")

# The 'messy' URL from the site source
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# 1. Download the file
print("Downloading...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # 2. Open the zip in memory using BytesIO
    # This avoids saving the .zip to disk if you only want the contents
    # io.BytesIO: This acts like a "virtual file." Instead of saving the
    # .zip to your hard drive, waiting, and then opening it, we keep the
    # data in your RAM and treat it like a file that zipfile can read.
    # z.extractall(): This is the "easy button." It takes every file inside
    #    the zip (the .shp, .dbf, .shx, etc.) and puts them in your specified folder.
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        
        # Define the output directory
        extract_path = "./natural_earth_data"
        
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)
            
        # 3. Extract all files
        z.extractall(extract_path)
        
        print(f"Success! Files extracted to: {os.path.abspath(extract_path)}")
        print("Extracted files:", z.namelist())
else:
    print(f"Error: Received status code {response.status_code}")


# 1. SETUP - Define names and URL
url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip"
zip_name = "countries_download.zip"
extract_folder = "ne_data_extracted"

headers = {'User-Agent': 'Mozilla/5.0'}

# 2. DOWNLOAD - Save the file to the disk
print("Step 1: Downloading the zip file...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # We save the 'content' (bytes) to a physical file on the computer
    with open(zip_name, "wb") as f:
        f.write(response.content)
    print(f"Done! You should now see '{zip_name}' in your folder.")
    
    # 3. EXTRACTION - Open the physical file we just saved
    print("Step 2: Extracting files...")
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(extract_folder):
        os.makedirs(extract_folder)
        
    # Open the actual file from the hard drive
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
        
    print(f"Step 3: Success! Look in the '{extract_folder}' folder for your shapefiles.")
    
else:
    print(f"Download failed. Status: {response.status_code}")

countries = extract_path + "ne_110m_admin_0_countries.zip"