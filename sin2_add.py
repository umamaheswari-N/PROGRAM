import matplotlib.pyplot as plt
import numpy as np
Fs=100
f=8
sample=100
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.subplot(311)
plt.plot(x,y)
Fs1=150
f1=8
sample=100
m=np.arange(sample)
n=np.sin(2*np.pi*f*m/Fs1)
plt.subplot(312)
plt.plot(m,n)

z=y+n
plt.subplot(313)
plt.plot(m,z)
plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()
