import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline  
plt.rcParams['axes.facecolor'] = '#f2f2f2'

import ipywidgets as widgets
from ipywidgets import interact
from ipywidgets import fixed

x = np.linspace(-1000,1000,2000)
Xp, Yp = np.meshgrid(x,x)
Xobs = [Xp, Yp, np.zeros(np.shape(Xp))]

def calc_sphere_gravity(xobs, xsrc, rho, src_radius):
    
    gamma = 6.67e-11
    r = np.sqrt((xobs[0] - xsrc[0])**2 + (xobs[1] - xsrc[1])**2 + (xobs[2] - xsrc[2])**2)
    gx = gamma * ((4/3.)*np.pi*rho*(src_radius**3)) * (xobs[0] - xsrc[0]) / r**3
    gy = gamma * ((4/3.)*np.pi*rho*(src_radius**3)) * (xobs[1] - xsrc[1]) / r**3
    gz = gamma * ((4/3.)*np.pi*rho*(src_radius**3)) * (xobs[2] - xsrc[2]) / r**3
    gx = gx*1e5 #convert to milligals
    gy = gy*1e5
    gz = gz*1e5
    
    return [gx, gy, gz]

def calc_slab_gravity(xobs, xsrc, zsrc, rho, slab_thickness):
    
    gamma = 6.67e-11
    x=xobs-xsrc
    gz = 2.*gamma * rho * slab_thickness * (np.pi/2.0 + np.arctan(x/zsrc)) 
    gz = gz*1e5
    
    return gz


def calc_cylinder_gravity(xobs, xsrc, rho, src_radius):
    
    gamma = 6.67e-11
    r = np.sqrt((xobs[0] - xsrc[0])**2 + (xobs[1] - xsrc[1])**2 + (xobs[2] - xsrc[2])**2)
    gx = gamma * ((2.)*np.pi*rho*(src_radius**2)) * (xobs[0] - xsrc[0]) / r**2
    gy = gamma * ((2.)*np.pi*rho*(src_radius**2)) * (xobs[1] - xsrc[1]) / r**2
    gz = gamma * ((2.)*np.pi*rho*(src_radius**2)) * (xobs[2] - xsrc[2]) / r**2
    gx = gx*1e5 #convert to milligals
    gy = gy*1e5
    gz = gz*1e5
    
    return [gx, gy, gz]

def plot_gravity_profile(x=0, y=0, z=-50, src_radius=40, rho=1000, obs_range=np.arange(-1000,1000,10)):
    
    xsrc = [x, 0, z]
    gravity_profile_z = []
    for x in obs_range:
        xobs = [x, y, 0]
        g = calc_sphere_gravity(xobs, xsrc, rho, src_radius)
        gravity_profile_z.append(g[2])
    fig, axarr1 = plt.subplots(2,sharex=True, figsize=(8,8))
    ax1=axarr1[0]
    
    ax1.plot(obs_range, gravity_profile_z, linewidth=4)
    ax1.set_ylabel(r'$g_z$ (mGal)', fontsize=18)

    ax2 = axarr1[1]

    yr1=ax2.get_xlim()
    ax2.set_ylim((yr1[0],0))
    circle = plt.Circle((xsrc[0],xsrc[2]),src_radius,color='#fc8d59')
    ax2.add_artist(circle)
    ax2.set_ylabel('z(m)', fontsize=18)
    ax2.set_xlabel('x(m)', fontsize=18,)
    
    plt.show()

def plot_gravity_profile_test(x=0, y=0, z=-50, src_radius=40, rho=1000, obs_range=np.arange(-1000,1000,10)):
    
    xsrc = [x, 0, z]
    gravity_profile_z = []
    for x in obs_range:
        xobs = [x, y, 0]
        g = calc_sphere_gravity(xobs, xsrc, rho, src_radius)
        gravity_profile_z.append(g[2])
    fig, ax1 = plt.subplots(1,figsize=(8,4))
    
    ax1.plot(obs_range, gravity_profile_z, linewidth=2)
    ax1.set_ylabel('Bouger Anomaly (mGal)', fontsize=18)
    ax1.set_xlabel('position (m)',fontsize=18)

    ax1.tick_params(axis='both', which='major', labelsize=14)
    ax1.tick_params(axis='both', which='minor', labelsize=14)

    ax1.grid(True,which='both')
    ax1.grid(which='minor',alpha=0.5)
    ax1.minorticks_on()

    plt.tight_layout()

    plt.savefig('TestPlot.png')

    plt.show()

def plot_gravity_profile_test_cylinder(x=0, y=0, z=-50, src_radius=40, rho=1000, obs_range=np.arange(-1000,1000,10)):
    
    xsrc = [x, 0, z]
    gravity_profile_z = []
    for x in obs_range:
        xobs = [x, y, 0]
        g = calc_cylinder_gravity(xobs, xsrc, rho, src_radius)
        gravity_profile_z.append(g[2])
    fig, ax1 = plt.subplots(1,figsize=(8,4))
    
    ax1.plot(obs_range, gravity_profile_z, linewidth=2)
    ax1.set_ylabel('Bouger Anomaly (mGal)', fontsize=18)
    ax1.set_xlabel('position (m)',fontsize=18)

    ax1.tick_params(axis='both', which='major', labelsize=14)
    ax1.tick_params(axis='both', which='minor', labelsize=14)

    ax1.grid(True,which='both')
    ax1.grid(which='minor',alpha=0.5)
    ax1.minorticks_on()

    plt.tight_layout()

    plt.savefig('TestPlot.png')

    plt.show()

def plot_two_sphere_profiles(x1=0.0,z1=200.0,rho1=1000., srad1=200.,x2 = 20.0, z2=-100, rho2=2000, srad2=100.):

    
#   x1=0.0
#    x2=20.0
#    y1=0.0
#    y2=0.0
#    z1=-50.0
#    z2=-100.0
#    s1=40
#    s2=80
#    rho1=1000
#    rho2=2000

    y1=0.0
    y2=0.0
    obs_range=np.arange(-1000,1000,10)
    
    x=[x1,x2]
    y=[y1,y2]
    z=[z1,z2]

    src_radius=[srad1,srad2]
    rho=[rho1,rho2]

    

    fig, axarr1 = plt.subplots(2,sharex=True, figsize=(8,8))
    
    cvec=['b','r']
    
    ax1=axarr1[0]
    ax2=axarr1[1]
 
    for ii in range(len(x)):
        xsrc = np.array([x[ii], 0.0, z[ii]])
        gravity_profile_z = []
        for x2 in obs_range:
            xobs = [x2, y, 0]
            g = calc_sphere_gravity(xobs, xsrc, rho[ii], src_radius[ii])
            gravity_profile_z.append(g[2])
    
   
        ax1.plot(obs_range, gravity_profile_z, linewidth=4,color=cvec[ii])
        circle = plt.Circle((xsrc[0],xsrc[2]),src_radius[ii],color=cvec[ii])
        ax2.add_artist(circle)

    ax1.set_ylabel(r'$g_z$ (mGal)', fontsize=18)
    yr1=ax2.get_xlim()
    ax2.set_ylim((yr1[0],0))
    ax2.set_ylabel('z(m)', fontsize=18)
    ax2.set_xlabel('x(m)', fontsize=18)
    
    plt.show()

def plot_sphere_cylinder_profiles(x1=0.0,z1=200.,rho1=1000., srad1=200.,x2 = 20.0, z2=-100, rho2=2000, srad2=100.):

    y1=0.0
    y2=0.0
    obs_range=np.arange(-1000,1000,10)
    
    x=[x1,x2]
    y=[y1,y2]
    z=[z1,z2]

    src_radius=[srad1,srad2]
    rho=[rho1,rho2]

    

    fig, axarr1 = plt.subplots(2,sharex=True, figsize=(8,8))
    
    cvec=['b','r']
    
    ax1=axarr1[0]
    ax2=axarr1[1]

    xsrc1 = np.array([x[0], 0.0, z[0]])
    xsrc2 = np.array([x[1], 0.0, z[1]])

 
    gravity_profile_z = []
    gravity_profile2_z = []
    for x2 in obs_range:
        xobs = [x2, y, 0]
        g = calc_sphere_gravity(xobs, xsrc1, rho[0], src_radius[0])
        gravity_profile_z.append(g[2])
        g2 = calc_cylinder_gravity(xobs,xsrc2,rho[1],src_radius[1])
        gravity_profile2_z.append(g2[2])

    
   
    ax1.plot(obs_range, gravity_profile_z, linewidth=4,color=cvec[0],label='sphere')
    ax1.plot(obs_range, gravity_profile2_z, linewidth=4,color=cvec[1],label='cylinder')
    circle = plt.Circle((xsrc1[0],xsrc1[2]),src_radius[0],color=cvec[0])
    ax2.add_artist(circle)
    circle = plt.Circle((xsrc2[0],xsrc2[2]),src_radius[1],color=cvec[1])
    ax2.add_artist(circle)

    


    ax1.legend()
    ax1.set_ylabel(r'$g_z$ (mGal)', fontsize=18)
    yr1=ax2.get_xlim()
    ax2.set_ylim((yr1[0],0))
    ax2.set_ylabel('z(m)', fontsize=18)
    ax2.set_xlabel('x(m)', fontsize=18)
    
    plt.show()

def plot_sphere_cylinder_slab_profiles(x1=0.0,z1=200.,rho1=1000., srad1=200.,
                                       x2 = 20.0, z2=-100, rho2=2000, srad2=100.,
                                       x3=0.0,z3=-200.,t3=100.,rho3=500.):

    y1=0.0
    y2=0.0
    obs_range=np.arange(-1000.,1000.,100)
    
    x=[x1,x2]
    y=[y1,y2]
    z=[z1,z2]

    src_radius=[srad1,srad2]
    rho=[rho1,rho2,rho3]

    

    fig, axarr1 = plt.subplots(2,sharex=True, figsize=(8,8))
    
    cvec=['b','r','k']
    
    ax1=axarr1[0]
    ax2=axarr1[1]

    xsrc1 = np.array([x[0], 0.0, z[0]])
    xsrc2 = np.array([x[1], 0.0, z[1]])

 
    gravity_profile_z = []
    gravity_profile2_z = []
    for x2 in obs_range:
        xobs = [x2, y, 0]
        g = calc_sphere_gravity(xobs, xsrc1, rho[0], src_radius[0])
        gravity_profile_z.append(g[2])
        g2 = calc_cylinder_gravity(xobs,xsrc2,rho[1],src_radius[1])
        gravity_profile2_z.append(g2[2])
    gravity_profile3_z = calc_slab_gravity(obs_range,x3,z3,rho[2],t3)
    
    
   
    ax1.plot(obs_range, gravity_profile_z, linewidth=4,color=cvec[0],label='sphere')
    ax1.plot(obs_range, gravity_profile2_z, linewidth=4,color=cvec[1],label='cylinder')
    ax1.plot(obs_range, gravity_profile3_z, linewidth=4,color=cvec[2],label='slab')
    circle = plt.Circle((xsrc1[0],xsrc1[2]),src_radius[0],color=cvec[0])
    ax2.add_artist(circle)
    circle = plt.Circle((xsrc2[0],xsrc2[2]),src_radius[1],color=cvec[1])
    ax2.add_artist(circle)

    yr1=ax2.get_xlim()
    ax2.set_ylim((yr1[0],0))
 
    
    slabx=[yr1[0],x3,x3,yr1[-1]]
    slabz=[z3-t3/2.,z3-t3/2,z3+t3/2,z3+t3/2]

    ax2.fill_between(slabx,slabz,yr1[0])

    
    ax2.set_xlim(yr1)

    ax1.legend()
    ax1.set_ylabel(r'$g_z$ (mGal)', fontsize=18)
    ax2.set_ylabel('z(m)', fontsize=18)
    ax2.set_xlabel('x(m)', fontsize=18)
    
    plt.show()

