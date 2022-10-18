import os
import numpy as np
import shutil
import time
import subprocess


def input(g):
    """ Function that reads the input from csv file and returns list for use annotation in the INPUTER.txt file
        
        Input:
                g: counter for the column number of currently processed sample in comp.txt
                
        Returns:
                mat: list with component amounts read from comp.txt file to be used as input in the program"""

    mat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fileo=np.loadtxt("comp.txt",dtype='str',delimiter="\t",unpack=False)
    n=0
    for c in fileo[:,0]:
        fr=fileo[n,g]
        if c in["SiO2","sio2"]:
            if float(fr) in[0,0.0,0.00]:
                mat[0]=0.0001
            else:
                mat[0]=float(fileo[n,g])
        if c in["TiO2","tio2"]:
            if float(fr) in[0,0.0,0.00]:
                mat[1]=0.0001
            else:
                mat[1]=float(fileo[n,g])
        if c in["Al2O3","al2o3"]:
            if float(fr) in[0,0.0,0.00]:
                mat[2]=0.0001
            else:
                mat[2]=float(fileo[n,g])
        if c in["Cr2O3","cr2o3"]:
            if float(fr) in[0,0.0,0.00]:
                mat[3]=0.0001
            else:
                mat[3]=float(fileo[n,g])
        if c in["FeO","feo"]:
            if float(fr) in[0,0.0,0.00]:
                mat[4]=0.0001
            else:
                mat[4]=float(fileo[n,g])
        if c in["MgO","mgo"]:
            if float(fr) in[0,0.0,0.00]:
                mat[5]=0.0001
            else:
                mat[5]=float(fileo[n,g])
        if c in["MnO","mno"]:
            if float(fr) in[0,0.0,0.00]:
                mat[6]=0.0001
            else:
                mat[6]=float(fileo[n,g])
        if c in["CaO","cao"]:
            if float(fr) in[0,0.0,0.00]:
                mat[7]=0.0001
            else:
                mat[7]=float(fileo[n,g])
        if c in["K2O","k20"]:
            if float(fr) in[0,0.0,0.00]:
                mat[8]=0.0001
            else:
                mat[8]=float(fileo[n,g])
        if c in["Na2O","na2o"]:
            if float(fr) in[0,0.0,0.00]:
                mat[9]=0.0001
            else:
                mat[9]=float(fileo[n,g])
            #Fe2O3
            mat[10]=0.0001
            mat[11]=0.0001
            mat[12]=0.0001
            mat[13]=0.0001
        
        n=n+1
    return (mat)

fileo=np.loadtxt("comp.txt",dtype='str',delimiter="\t",unpack=False)
j=1
if os.path.exists("Results"):
    shutil.rmtree("Results")
if os.path.exists("INPUTER.txt"):
    os.remove("INPUTER.txt")

os.mkdir("Results")
for d in fileo[0,1:]:
    os.mkdir("Results/"+str(d))
    e="Results/"+str(d)
    if os.path.exists(str(e)+"/plot.sh"):
        os.remove(str(e)+"/plot.sh")
    if os.path.exists(str(e)+"/plot.ps"):
        os.remove(str(e)+"/plot.ps")
    if os.path.exists(str(e)+"/plot.pdf"):
        os.remove(str(e)+"/plot.pdf")

    if os.path.exists("INPUTER.txt"):
        os.remove("INPUTER.txt")
    if os.path.exists ("MAGFOX.XTL"):
        os.remove("MAGFOX.XTL")
    if os.path.exists ("MAGFOX.WFX"):
        os.remove("MAGFOX.WFX")
    if os.path.exists ("MAGFOX.LIQ"):
        os.remove("MAGFOX.LIQ")
    if os.path.exists ("MAGFOX.DAT"):
        os.remove("MAGFOX.DAT")
    
    pressure = 2
    z=input(j)
    filex=open("INPUTER.txt","x")
    filex.write("2"+"\n"+str(d)+"\n"+str(z[0])+"\n"+str(z[1])+"\n"+str(z[2])+
                "\n"+str(z[3])+"\n"+str(z[4])+"\n"+str(z[5])+"\n"+str(z[6])+
                "\n"+str(z[7])+"\n"+str(z[8])+"\n"+str(z[9])+"\n"+str(z[10])+
                "\n"+str(z[11])+"\n"+str(z[12])+"\n"+str(z[13])+"\n"+
                "0.01\n"+ #crystallization step
                "0.99\n"+ # crystallization endpoint
                str(float(pressure))+
                "\n"+
                "2"+ # temperature options (1 for old lunar; 2 for New Langmuir)
                "\n"+
                "0") # Type of output (0;1;2)
    filex.close()
    a=subprocess.Popen("./a.out")
    a.wait()
    print("finished")

    shutil.copy("MAGFOX.XTL","Results/"+str(d)+"/xtl"+str(pressure)+".txt")
    xtl=open("Results/"+str(d)+"/xtl"+str(pressure)+".txt", "r",encoding="ISO-8859-1")
    data=xtl.read()
    data= data.replace(" ","")
    xtl.close()
    xtl=open("Results/"+str(d)+"/xtl"+str(pressure)+".txt","w")
    xtl.write(data)
    xtl.close()
    shutil.copy("MAGFOX.LIQ","Results/"+str(d)+"/liq"+str(pressure)+".txt")
    shutil.copy("MAGFOX.DAT","Results/"+str(d)+"/dat"+str(pressure)+".txt")
    shutil.copy("MAGFOX.WFX","Results/"+str(d)+"/wfx"+str(pressure)+".txt")
        
    j=j+1
