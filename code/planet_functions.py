import numpy as np
import matplotlib.pyplot as plt 

def eccentricity(x,y,L,l):

  rj=(x**2+y**2)**.5
  e=np.zeros(int(L/l), dtype=float);
  for i in range(0,int(L/l)):
    win=range(i*l*365,(i+1)*l*365)
    a=max(rj[win])
    b=min(rj[win])
    e[i]=1-2/(a/b+1)
  return e

def figure_orbit(x,y,xJ,yJ,e):

  fig=plt.figure(1,figsize=(12,5))
  ax=fig.add_subplot(1,2,1)
  ax.plot(x,y)
  ax.plot(xJ,yJ)
  ax.plot (0,0,'o')
  ax.set_aspect('equal', 'box')

  ax=fig.add_subplot(1,2,2)
  ax.plot(range(0,len(e)),e)

  figname='../Figures/planet_earthJupiter2.png'

  plt.savefig(figname, dpi=100, bbox_inches='tight')
