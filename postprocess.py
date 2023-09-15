import os,glob,shutil,time
from PIL import Image

import argparse

parser = argparse.ArgumentParser(
                    prog = 'copies floppies',
                    description = 'floppier floppy copier')

parser.add_argument("FloppyDirectory", type=str)
parser.add_argument("OutputDirectory", type=str)

args = parser.parse_args()

floppy = args.FloppyDirectory
dest = args.OutputDirectory

localtime = time.localtime()

timedir = str(localtime.tm_mon)+"-"+str(localtime.tm_mday)+"-"+str(localtime.tm_year)

sessiondir = dest+"/"+timedir

if not os.path.exists(sessiondir):
    print("Making Directory: "+sessiondir)
    os.mkdir(sessiondir)
else:
    print("Directory "+sessiondir+" already exists, using...")

try:
    curflop = max([int(s.replace('floppy-','')) for s in next(os.walk(sessiondir))[1]]) + 1
except:
    curflop = 1

workingdir = ""

while True:
    workingdir = sessiondir+"/floppy-"+str(curflop)

    input("Press any key to copy that floppy...")
    files = glob.glob(floppy+"*")
    if len(files) == 0:
        print("There is no floppy to copy!!! (or it contains no files.)")
    else:
        os.mkdir(workingdir)
        print("Created Directory: "+workingdir)

        for file in files:

            print("Copying file "+file+" to "+workingdir+" ...")

            try:
                shutil.copy2(file, workingdir)
            except:
                print("Error copying file: "+file+"! Skipping...")

        for file in files:
            print("Deleting file "+file+" ...")
            try:
                os.remove(file)
            except:
                print("Error deleting file: "+file+"! Skipping...")
        curflop += 1
        print("Done!\n")
