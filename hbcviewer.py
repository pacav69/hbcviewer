#
# Python program to read brew cask taps and display
# a description and a screenshot
import os
import csv
import pprint

# read the contents of a directory to create a filelist
# of casks
# caskfiledir="/usr/local/Library/Taps/caskroom/homebrew-cask/production_Casks"
caskfiledir = "./Casks"
caskdescriptiondir = "./description/"
caskscreenshotdir = "./screenshots/"
caskfilelist = []
for filename in os.listdir(caskfiledir):
    if filename.endswith('.rb'):
        # remove extension from filename
        filenamesplitup = str.rstrip(filename, ".rb")
        # add to the caskfilelist
        caskfilelist.append(filenamesplitup + "\n")
        # check if file exists
        # if os.path.isfile(caskdescriptiondir+filenamesplitup+".csv"):
        #     print ("the file " +filenamesplitup+ " already exists")
        #     # create a description file
        # else:
        print ("the file " + filenamesplitup + " is being created")
        caskfilecreate = open(caskdescriptiondir + filenamesplitup + ".csv", 'w')
        caskfilecreate.write("filename:[" + filenamesplitup + "]")
        caskfilecreate.write("\n")
        caskfilecreate.write("description:[" + "none" + "]")
        caskfilecreate.write("\n")
        caskfilecreate.write("shortcut:[" + "brew " + "cask " + "install " + filenamesplitup + "]")
        caskfilecreate.write("\n")
        gethp = open(caskfiledir + "/" + filename)
        gethomepage = gethp.read('homepage')
        # gethomepage = "myhomepage"
        caskfilecreate.write("homepage:[" + gethomepage + "]")
        caskfilecreate.close()
        # create an empty screenshot file
        caskscreenshotcreate = open(caskscreenshotdir + filenamesplitup + ".png", 'w')
        caskscreenshotcreate.close()  # gethomepageroutine()
#         gethp=open(filename,'r')
#         return homepage


# add a caskfiledesc
# caskfileadddesc()
#
# # delete a caskfiledesc
# caskfiledeletedesc()
#
# # edit a caskfiledesc
# caskfileeditdesc()
#
# # submit a caskfiledesc
# caskfiledescsubmit()
#
# # add a screenshotfile
# addscreenshotfile()
#
# # copy shortcut to clipboard
# copy_shortcut_to_clipboard()


# caskfilelist.sort(key / str.lower)
print caskfilelist
caskfilesfound = open('casklist.txt', 'w')
caskfilesfound.writelines(caskfilelist)
caskfilesfound.close()

# create an empty file with the filename from the list of files
# stored in the casklist.txt file
# caskdesc = open('casklist.txt', 'r')
# for filename in
# caskdescriptiondir
# caskdesc.close()
