import numpy as np
from matplotlib import pyplot as plt
import random

#setting seeds for random functions so the resulting generated numbers are the same
def set_seeds(seed=100):
    random.seed(seed)
    np.random.seed(seed)

set_seeds()

x=np.linspace(0,10,100)

y=x+np.random.standard_normal(len(x))
#polyfit gives me the coefficients
reg=np.polyfit(x,y,deg=1)
print(reg)
plt.figure(figsize=(10,6))
plt.plot(x,y,'bo',label='Data')
# takes the coeficients from reg and then computes the y-values for the line
plt.plot(x,np.polyval(reg,x),'r',lw=2,label='Linear regression')
plt.legend(loc='best')

plt.show()

