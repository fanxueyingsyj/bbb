import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)
s=np.sin(x)
c=np.cos(x)
plt.plot(x,s,linestyle='--',color='r',linewidth=0.5)
plt.plot(x,c,linestyle='-',color='blue',linewidth=2)
plt.show()
