import os,sys

def spoof(sp):
        name = sp.split(".")[0]
        newname = os.getcwd()+os.sep+name+u"\u202E"
        os.mkdir(newname)
spoof("  ")
