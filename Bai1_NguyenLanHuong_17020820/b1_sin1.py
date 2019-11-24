import matplotlib.pyplot as plt
import numpy as np

fs = 100
f =2
N = 100
A = 5
x = np.arange(N)
s2 = A*np.sin(2*np.pi*f*(x/fs))
print(x)
print(s2)

plt.plot(x,s2)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.savefig("wave_sin1.jpg")
plt.show()
