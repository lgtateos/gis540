import os, sys, zipfile

inDir = sys.argv[1]

files = os.listdir(inDir)

outZipName = os.path.basename(inDir) + ".zip"

tFile = zipfile.ZipFile(indir + "/" + outZipName, "w")

for f in files:
    tFile.write(inDir + "/" + f, f, zipfile.ZIP_DEFLATED)

tFile.close()
                