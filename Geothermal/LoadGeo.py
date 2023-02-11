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
    minor_ticks = np.arange(0, sigmax, 1)
    plt.gca().set_xticks(minor_ticks,minor=True)
    minor_ticks = np.arange(0, taumax, 1)
    major_ticks = np.arange(0, taumax, 5)
    plt.gca().set_yticks(minor_ticks,minor=True)
    plt.gca().set_yticks(major_ticks)
    plt.grid(which='both')
    plt.show()

def Mohr_Failure():
    clean = interactive(Mohr_Failure_Figure,p=(0,20,.1),mu=(0.5,.8,.05),sig1=(2,20,1),sig2=(6,30,1))
    return clean 

def calculate_angle(sigma_fail=6,tau_fail=8,sig1=8,sig2=22,p=4):
#calculate the angle of failure for the given coordinates.  
#The coordinates will be on the Mohr circle, where it meets the failure curve
#Inputs: 
#.    sigma_fail x-coordinate of the crossing point
#.    tau_fail.  y-coordinate of the crossing point
#.Outputs:
#     theta: the failure angle
    mohr_cen=(sig1+sig2)/2-p
    x_dist=mohr_cen-sigma_fail
    pi_twotheta=np.arctan2(tau_fail,x_dist)
    twotheta=np.pi-pi_twotheta
    theta=twotheta/2.
    return theta*180/np.pi
