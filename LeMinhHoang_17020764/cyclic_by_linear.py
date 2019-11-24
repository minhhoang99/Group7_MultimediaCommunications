import numpy as np

def convolve(a, b):
    longer = [a, b][np.argmax((len(a), len(b)))]
    shorter = [b, a][np.argmin((len(b), len(a)))]
    K = len(longer)-len(shorter)+1
    convolution = np.zeros(K, longer.dtype)
    for i in range(K):
        convolution[i] = np.dot(longer[i:len(shorter)+i], shorter[::-1])
    return convolution

def circular_convolution(a, b):
    return convolve(np.hstack((a[-len(b)+1:], a)), b)

def linear_by_circular(a, b):
    return circular_convolution(np.pad(a, (0, len(b)-1), mode='constant', constant_values=0.0), b)

a = np.array([1,2,3]) #mảng a
b = np.array([3,4,5]) #mảng b

# a = np.random.normal(0.0, 1.0, 100)
# b = np.random.normal(0.0, 1.0, 21)
print(np.allclose(linear_by_circular(a, b), np.convolve(a, b, mode='same')))

print(a)
print(b)

print(np.convolve(a, b, mode='same'))