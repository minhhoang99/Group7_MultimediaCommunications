import math
import numpy as np
import matplotlib.pyplot as plt

#tần số cơ bản
f = 60.0
#chu kì
T = 1 / f
#số chu kì tín hiệu cần vẽ
N = 5
#tần số lấy mẫu
fs = 2000
#biên độ
A = 10

t = np.arange(0, N * T , N * T / float(fs))
print (np.shape(t))

n = 10

sin_wave = np.zeros(fs)
print (np.shape(sin_wave))

for i in range(2 * n + 1):
  
        print (i)
        i1 = math.pow(1/(2 * float(i) + 1), 2)
        s2 = A * i1 * np.sin(2 * math.pi * ( 2 * i + 1) * f * t)
        sin_wave += s2

plt.plot(t, sin_wave, label='sin_wave')
plt.xlabel('t')
plt.ylabel('sin_wave')
plt.savefig("wave_sin2.jpg")
plt.show()
