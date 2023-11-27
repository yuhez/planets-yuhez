
#planet with Jupiter
import numpy as np
import matplotlib.pyplot as plt 

#constants
G=6.6743e-11
AU=149.597871e9 # 1 astronomical unit (AU) is the mean distance between sun and Earth
AU1=150.8e9
dJ=5.203*AU
mj=5.97219e24
mJ=1.899e27
M=1.9891e30
day=86400;
year=31556926;
v0=AU*2*np.pi/year;

#Jupiter
v0J=dJ*2*np.pi/(11.86*year);

L=50000

x0=AU1;
y0=0;
u0=0;
x=np.zeros(365*L, dtype=float);
y=np.zeros(365*L, dtype=float);


x[0]=x0;
y[0]=y0;
u=u0;
v=v0;

x0J=dJ;
y0J=0;
u0J=0;
xJ=np.zeros(365*L, dtype=float);
yJ=np.zeros(365*L, dtype=float);
xJ[0]=x0J;
yJ[0]=y0J;
uJ=u0J;
vJ=v0J;

for i in range(1,365*L):    
    if i % 36500==0:
        print(i/365)

    x[i]=x[i-1]+day*u;
    y[i]=y[i-1]+day*v;
    xJ[i]=xJ[i-1]+day*uJ;
    yJ[i]=yJ[i-1]+day*vJ;
    
    axS=-G*M/(abs(x[i]**2+y[i]**2)**[3/2])*x[i];
    ayS=-G*M/(abs(x[i]**2+y[i]**2)**[3/2])*y[i];
    dxJ=x[i]-xJ[i];
    dyJ=y[i]-yJ[i];
    axEJ=-G*mJ/(abs(dxJ**2+dyJ**2)**[3/2])*dxJ;
    ayEJ=-G*mJ/(abs(dxJ**2+dyJ**2)**[3/2])*dyJ;
    ax=axS+axEJ;
    ay=ayS+ayEJ;

    u=u+ax*day;
    v=v+ay*day;

    axJ=-G*M/(abs(xJ[i]**2+yJ[i]**2)**[3/2])*xJ[i];
    ayJ=-G*M/(abs(xJ[i]**2+yJ[i]**2)**[3/2])*yJ[i];
    uJ=uJ+axJ*day;
    vJ=vJ+ayJ*day;


rj=(x**2+y**2)**.5

l=1000;
e=np.zeros(int(L/l), dtype=float);
for i in range(0,int(L/l)):
    win=range(i*l*365,(i+1)*l*365)
    a=max(rj[win])
    b=min(rj[win])
    e[i]=1-2/(a/b+1)

fig=plt.figure(1,figsize=(12,5))
ax=fig.add_subplot(1,2,1)
ax.plot(x,y)
ax.plot(xJ,yJ)
ax.plot (0,0,'o')


ax=fig.add_subplot(1,2,2)
ax.plot(range(0,int(L/l)),e)

plt.savefig('../Figures/planet_earthJupiter.png', dpi=100, bbox_inches='tight')