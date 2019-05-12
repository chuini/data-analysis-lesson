import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x)+ 1
z = np.cos(x**2)+1
plt.figure(figsize = (8,4))
plt.plot(x,y,label = '$\sinx +1$',color = 'red',linewidth =2)
plt.plot(x,z, 'bp--' , label = '$\cosx^2 +1$')
plt.xlabel('time(s)')
plt.ylabel('volt')
plt.title('simple')
plt.ylim(0,2.2)
plt.legend()
plt.show()
