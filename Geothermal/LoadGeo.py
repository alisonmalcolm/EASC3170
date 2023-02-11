import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, IntSlider, widget, FloatText, FloatSlider
import matplotlib
font = {'size'   : 16}

matplotlib.rc('font', **font)

def Mohr_Failure_Figure(p=0.,mu=0.8,sig1=8,sig2=22):
    taumax=20
    sigmax=35
    sigma=np.arange(0,sigmax)
    tau=np.arange(0,taumax)
    th=np.arange(-np.pi/2,np.pi/2,np.pi/100)
    fig = plt.figure(figsize=(10, 6))
    mohr_rad=(sig2-sig1)/2
    mohr_cen=(sig1+sig2)/2-p
    mohr_x=mohr_cen+mohr_rad*np.sin(th)
    mohr_y=mohr_rad*np.cos(th)
    plt.plot(mohr_x,mohr_y)
    plt.ylim([0,np.max(tau)])
    plt.xlim([0,np.max(sigma)])
    tau_fail=mu*sigma
    plt.plot(sigma,tau_fail)
    plt.xlabel(r"$\sigma_n$ (MPa)")
    plt.ylabel(r"$\tau$ (MPa)")
    plt.show()

def Mohr_Failure():
    clean = interactive(Mohr_Failure_Figure,p=(0,20,.1),mu=(0.5,.8,.05),sig1=(2,20,1),sig2=(6,30,1))
    return clean 
