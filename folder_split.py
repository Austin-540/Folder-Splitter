sizelimit_MB = 200 #MB


inpdir = "inputf/"
outdir = "outputf/"
sizelimit = sizelimit_MB * 1000 * 1000 #B

import os
import shutil

sizesofar = 0
dircount = 1

filecount = 0
os.mkdir(outdir+str(dircount))

for path in os.listdir(inpdir):
    # check if current path is a file
    if os.path.isfile(os.path.join(inpdir, path)):
        filecount += 1


        print(sizesofar + os.path.getsize(os.path.join(inpdir, path)))
        if sizesofar + os.path.getsize(os.path.join(inpdir, path)) >= sizelimit:
            dircount += 1
            sizesofar = 0
            os.mkdir(outdir+str(dircount))


        shutil.move(inpdir+path, outdir+str(dircount)+"/")
        

        total_size = 0


        for dirpath, dirnames, filenames in os.walk(outdir+str(dircount)+"/"):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)



        sizesofar = total_size
        print(sizesofar)
        
        


print('File count:', filecount)