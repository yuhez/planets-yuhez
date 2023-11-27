import numpy as np

def acc_effect(G,M,x,y):

    ax=-G*M/(abs(x**2+y**2)**[3/2])*x;
    ay=-G*M/(abs(x**2+y**2)**[3/2])*y;

    return ax, ay

def planet_motion(G,M,x,y,u,v,day):
        
    ax=-G*M/(abs(x**2+y**2)**[3/2])*x;
    ay=-G*M/(abs(x**2+y**2)**[3/2])*y;
    u=u+ax*day;
    v=v+ay*day;
    
    return u, v
    