#planet with Jupiter
import numpy as np
from  planet_functions import *
from  planet_data import *
from  planet_iter import *

L=400 #number of years to simulate

G,AU,M,day,year=general_constants()

# Get the mass and the initial position of Earth
x,y,u,v,mj=init_Earth(AU,year,L)

# Get the mass and the initial position of Jupiter
xJ,yJ,uJ,vJ,mJ=init_Jupiter(AU,year,L)

for i in range(1,365*L):    
    #Counter for each 100 years
    if i % 36500==0:
        print(i/365)
        
    # New positions of Earth
    x[i]=x[i-1]+day*u;
    y[i]=y[i-1]+day*v;
    
    # New positions of Jupiter
    xJ[i]=xJ[i-1]+day*uJ;
    yJ[i]=yJ[i-1]+day*vJ;
    
    # acceleration of Earth due to Sun
    axS, ayS = acc_effect(G,M,x[i],y[i])    
        
    # acceleration of Earth due to Jupiter
    dxJ=x[i]-xJ[i];
    dyJ=y[i]-yJ[i];
    axEJ, ayEJ = acc_effect(G,mJ,dxJ,dyJ)  
    
    # net effect on velocity of Earth
    ax=axS+axEJ;
    ay=ayS+ayEJ;
    u=u+ax*day;
    v=v+ay*day;

    # new velocity of Jupiter
    uJ,vJ = planet_motion(G,M,xJ[i],yJ[i],uJ,vJ,day)

    
l=100
e=eccentricity(x,y,L,l)

figure_orbit(x,y,xJ,yJ,e)
