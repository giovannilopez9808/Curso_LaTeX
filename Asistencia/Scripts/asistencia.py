import numpy as np
from os import listdir
#<-----------------------------Localizacion de archivos------------------>
dir="../Archivos/"
#<-----------------------------Archivos---------------------------------->
files=listdir(dir)
#<--------------------------Inicializacion de los datos-------------------->
ids=[];counts=[]
for file in files:
    #<---------------------------------------Lectura de asistencias--------------------->
    data=np.loadtxt(dir+file,skiprows=1,usecols=1,dtype=str,delimiter=",")
    #<----------------------------Personas nuevas------------------------------>
    new=list(set(data)-set(ids))
    #<------------------------Adiccion de las personas nuevas-------------------->
    counts=np.append(counts,np.zeros(np.size(new)))
    ids=np.append(ids,new)
    #<------------------------------numero de personas totales---------------------->
    n_persons=np.size(ids)
    for i in range(n_persons):
        #<----------------------------encontrar el registro----------------------->
        found=np.size(np.where(ids[i]==data)[0])
        if found!=0:
            #<-----------------------------Suma------------------------>
            counts[i]+=1
assistance_file=open("../Asistencia.csv","w")
assistance_file.write("Matricula,asistencias\n")
for id,count in zip(ids,counts):
    assistance_file.write(id[1:8]+","+str(int(count))+"\n")
assistance_file.close()