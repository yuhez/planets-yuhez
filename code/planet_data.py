import numpy as np

def general_constants():
#  global G, M, AU, day, year
  G=6.6743e-11
  AU=149.597871e9
  M=1.9891e30
  day=86400;
  year=31556926;
  
  return G,AU,M,day,year

def init_Earth(AU,year,L):

  mj=5.97219e24
  AU1=150.8e9
    
  x0=AU1;
  v0=AU*2*np.pi/year;
  y0=0;
  u0=0;
  x=np.zeros(365*L, dtype=float);
  y=np.zeros(365*L, dtype=float);
  x[0]=x0;
  y[0]=y0;
  u=u0;
  v=v0;
  
  return x,y,u,v,mj

def init_Jupiter(AU,year,L):
  dJ=5.203*AU
  mJ=1.899e27
  v0J=dJ*2*np.pi/(11.86*year);

  x0J=dJ;
  y0J=0;
  u0J=0;
  xJ=np.zeros(365*L, dtype=float);
  yJ=np.zeros(365*L, dtype=float);
  xJ[0]=x0J;
  yJ[0]=y0J;
  uJ=u0J;
  vJ=v0J;
  
  return xJ,yJ,uJ,vJ,mJ
