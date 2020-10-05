import numpy as np
import matplotlib.pyplot as plt
font = {'family': 'serif',
        'color':  'white',
        'size': 12,
        }
dir_graphics="images/"
percentages=np.array([[0,25],[25,75],[75,100]])
colors=["#80ffdb","#64dfdf","#5390d9"]
data=np.loadtxt("cloud_factor.dat")
for percentage,color in zip(percentages,colors):
   # plt.fill_between(percentage,[0,100],color=color,alpha=0.75)
    for value in percentage:
        plt.plot([value,value],[0,100],ls="--",color="black",alpha=0.7)
plt.ylim(0,1);plt.xlim(0,100)
plt.yticks(np.arange(0,1+0.1,0.1));plt.xticks(np.arange(0,110,10))
plt.text(4,0.5,"   Cielo\ndespejado\n    C$_f$=1",fontdict=font)
plt.text(44,0.5," Medio\nnublado\n C$_f$=0.9",fontdict=font)
plt.text(77.5,0.52," Nublado\n  C$_f$=0.6",fontdict=font)
plt.ylabel("Factor de nubes");plt.xlabel("Porcentaje de nubes (%)")
plt.plot(data[:,0],data[:,1],ls="--",color="#56cfe1",lw=3)
plt.savefig(dir_graphics+"cloud2.png",dpi=200,transparent=True)
plt.show()