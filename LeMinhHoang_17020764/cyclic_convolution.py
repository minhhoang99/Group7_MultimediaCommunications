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

a = np.array([1,2,3]) #mảng a
b = np.array([3,4,5]) #mảng b

print(a)
print(b)

print(np.allclose(circular_convolution(a, b), np.fft.ifft(np.fft.fft(a)*np.fft.fft(b))))
print(np.convolve(a, b, mode='same'))