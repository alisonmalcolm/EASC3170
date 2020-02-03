import numpy as np
import math
import matplotlib.pyplot as plt
#%matplotlib inline
#try:
from ipywidgets import  interact, interactive, IntSlider, widget, FloatText, FloatSlider
#    pass
#except Exception, e:    
#    from ipywidgets import interact, interactive, IntSlider, widget, FloatText, FloatSlider

dat=np.loadtxt('ComputedData.txt')
offset=dat[:,0]
ttime1=dat[:,1]
ttime2=dat[:,2]

def PlotTraveltimes(offset,ttime1,ttime2):
    plt.plot(offset,ttime1,offset,ttime2)
    plt.xlabel('offset (m)')
    plt.ylabel('time (s)')
    plt.ylim([2.8,1.8])
    plt.grid()
    plt.title('Traveltime Data')
    plt.show()

def NMOPlot(vel):
    plt.plot(offset,ttime1,'b',label='data')
    plt.plot(offset,ttime2,'b')
    plt.xlabel('offset (m)')
    plt.ylabel('time (s)')
    plt.ylim([2.8,1.8])
    plt.grid()
    tNMO=offset**2/2/vel**2/ttime1
    t_Corrected1=ttime1-tNMO
    tNMO2=offset**2/2/vel**2/ttime2
    t_Corrected2=ttime2-tNMO
    plt0, =plt.plot(offset,t_Corrected1,'r',label='NMO corrected')
    plt1, =plt.plot(offset,t_Corrected2,'r')
    plt.legend(loc=3)
    plt.show()

def InteractNMO():
    NMO = interactive(NMOPlot,vel=(600,1800,50))
    return NMO
