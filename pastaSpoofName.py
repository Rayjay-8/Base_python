import os,sys

def spoof(sp):
        name = sp.split(".")[0]
        path = sp.split(".")[1]
        print(sp)
        print(name)
        print(path)
        
        #newname = os.getcwd()+os.sep+name+u"\u202E"
        newname = name+u"\u202E"+"TXT."+path
        print(newname)
        #os.mkdir(newname)
        with open(newname,"w") as tk:
                tk.write("")
#spoof("teste.exe")
ffile = 'tetes.lnk'
print(os.listdir("."))
os.rename(ffile,"teste.lnk"+u"\u202E"+" TXT. ")
