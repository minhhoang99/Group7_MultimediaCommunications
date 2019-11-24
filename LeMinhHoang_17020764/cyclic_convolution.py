import numpy as np

#tính trực tiếp cyclic convolution
def convolve(a, b):
    longer = [a, b][np.argmax((len(a), len(b)))]
    shorter = [b, a][np.argmin((len(b), len(a)))]
    K = len(longer)-len(shorter)+1
    convolution = np.zeros(K, longer.dtype)
    for i in range(K):
        convolution[i] = np.dot(longer[i:len(shorter)+i], shorter[::-1])
    return convolution

def cyclic_convolution(a, b):
    return convolve(np.hstack((a[-len(b)+1:], a)), b)

#Tạo 2 vector ngẫu nhiên
# a = np.random.normal(0.0, 1.0, 100)
# b = np.random.normal(0.0, 1.0, 11)
a = np.array([1,2,3]) #mảng a
b = np.array([3,4,5]) #mảng b

print("Mảng a:", a)
print("Mảng b:", b)

#Kết quả khi dùng hàm có sẵn với chế độ mode=same
print("Kết quả tích chập khi dùng hàm có sẵn:", np.convolve(a, b, mode='same'))

print("Kết quả khi tính tích chập trực tiếp:", np.fft.ifft(np.fft.fft(a)*np.fft.fft(b)))

#So sánh kết quả khi tính trực tiếp và dùng hàm có sẵn của scipy/python
print("So sánh:", np.allclose(cyclic_convolution(a, b), np.fft.ifft(np.fft.fft(a)*np.fft.fft(b))))

#Mảng c kiểu boolean để so sánh kết quả tính trực tiếp và kết quả khi dùng hàm có sẵn
c = np.in1d(cyclic_convolution(a, b), np.fft.ifft(np.fft.fft(a)*np.fft.fft(b)))
print(c)
