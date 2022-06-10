# -*- coding: utf-8 -*-
#%%
#Exo1 Tp3
#%%
import numpy as np
l1=list(range(10000))

#%%
import numpy as np
l1=list(range(10000))
l2=list(range(10000))
a1=np.array(range(10000))
a2=np.array(range(10000))
%timeit [l1[i]+l2[i] for i in range(10000)]
%timeit list(map(lambda x,y:x+y,l1,l2))
%timeit a1+a2

#%%
help(np.arange)
help(np.linspace)

#%%
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,num=10)
y=np.sin(x)

plt.plot(x,y, 'ro-')
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,2*np.pi,step=0.2)
y=np.sin(x)
plt.plot(x,y, 'ro-')
plt.show()

