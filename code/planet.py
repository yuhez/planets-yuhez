#planet
import numpy as np
import matplotlib.pyplot as plt 

#constants
G=6.6743e-11
AU=149.597871e9 # 1 astronomical unit (AU) is the mean distance between sun and Earth
AU1=150.8e9
mj=5.97219e24
mJ=1.899e27
M=1.9891e30
day=86400;
year=31556926;
v0=AU*2*np.pi/year;
Fg=G*M*mj/AU**2
ag=Fg/mj
Fc=mj*v0**2/AU
ac=Fc/mj

L=2

x0=AU1;
y0=0;
u0=0;
x=np.zeros(365*L, dtype=float);
y=np.zeros(365*L, dtype=float);

x[0]=x0;
y[0]=y0;
u=u0;
v=v0;

for i in range(1,365*L):    
    print(i)
    x[i]=x[i-1]+day*u;
    y[i]=y[i-1]+day*v;
    ax=-G*M/(abs(x[i]**2+y[i]**2)**[3/2])*x[i];
    ay=-G*M/(abs(x[i]**2+y[i]**2)**[3/2])*y[i];
    u=u+ax*day;
    v=v+ay*day;

rj=(x**2+y**2)**.5
a=max(rj)
b=min(rj)
e=1-2/(a/b+1)
rel=(a/b-1)


fig=plt.figure(1,figsize=(12,5))
ax=fig.add_subplot(1,2,1)
ax.plot(x,y)
ax.plot (0,0,'o')
#axis equal

ax=fig.add_subplot(1,2,2)
ax.plot(range(0,365*2),rj)

plt.savefig('../Figures/planet_earth.png', dpi=100, bbox_inches='tight')