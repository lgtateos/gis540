# Purpose: Unzip a file and write the results to a folder.
import zipfile
import os

zip_dir = "C:/gispy/scratch/"
zip_fullname = zip_dir + "countries.zip"
zip_path = os.path.splitext(zip_fullname)[0]
print("Extracting files...")

extract_folder = os.path.splitext(zip_path)[0]
# Create the output folder if it doesn't exist
if not os.path.exists(extract_folder):
    os.makedirs(extract_folder)
    
# Open the actual file from the hard drive
with zipfile.ZipFile(zip_fullname, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)
    
    print(f"Success! Files extracted to: {zip_path}")
    print("Extracted files:", zip_ref.namelist())