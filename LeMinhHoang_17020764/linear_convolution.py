import numpy as np

#Tính linear convolution trực tiếp
def convolve(a, b):
    longer = [a, b][np.argmax((len(a), len(b)))]
    shorter = [b, a][np.argmin((len(b), len(a)))]
    K = len(longer)-len(shorter)+1
    convolution = np.zeros(K, longer.dtype)
    for i in range(K):
        convolution[i] = np.dot(longer[i:len(shorter)+i], shorter[::-1])
    return convolution

#Lấy ngẫu nhiên 2 vector
# a = np.random.normal(0.0, 1.0, 100)
# b = np.random.normal(0.0, 1.0, 11)

a = np.array([1,2,3]) #Mảng a
b = np.array([3,4,5]) #Mảng b

print("Mảng a:", a)
print("Mảng b:",b)

#Kết quả khi tính trực tiếp
print("Kết quả khi tính trực tiếp:", (convolve(np.pad(a, (len(b)-1, len(b)-1), mode='constant', constant_values=0.0), b)))

#Kết quả khi dùng hàm có sẵn
print("Kết quả khi dùng hàm có sẵn:", np.convolve(a, b, mode='full'))

#So sánh kết quả tính trực tiếp và kết quả khi dùng hàm có sẵn của scipy/python
print("So sánh:", np.allclose(np.convolve(a, b, mode='full'),
            convolve(np.pad(a, (len(b)-1, len(b)-1), mode='constant', constant_values=0.0), b)))

#Mảng c kiểu boolean để so sánh kết quả tính trực tiếp và kết quả khi dùng hàm có sẵn
c = np.in1d(np.convolve(a, b, mode='full'),
            convolve(np.pad(a, (len(b)-1, len(b)-1), mode='constant', constant_values=0.0), b))
print(c)