Primero
import numpy as np
papas = np.random.rand(4,8)
print(papas)
papas[:,-1] = -1
papas[1,:] = 2
print(papas)

papa = np.random.normal(size=1000)
sabanera = (papa>2.0)
print(papa[sabanera])
print("Es cercano pues "+ str(len(papa[sabanera]))+ " es cercano al 2,275% como se espera lo mayor a dos veces la desviacion estandar")  

papas=np.random.normal(size=1000)
pastusas = (papas>0)
sabaneras = (papas<0)
papas[pastusas]=1
papas[sabaneras]=-1
print(papas)

Segundo

import matplotlib 
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt 

papas = np.linspace(0,2*np.pi,300)
plt.plot(np.sin(5*papas),np.sin(4*papas))

