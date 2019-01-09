import matplotlib.pyplot as plt
import numpy as np
Fs=100
f=9
sample=100
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.plot(x,y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()
