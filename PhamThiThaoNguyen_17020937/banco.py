import numpy as np
import matplotlib.pyplot as plt

print("Nhap vao so n: ")
n = int(input())
chessboard = np.zeros((n, n))
chessboard[1::2, 0::2] = 1
chessboard[0::2, 1::2] = 1

plt.imshow(chessboard, cmap ='binary')
# plt.show()
plt.savefig('banco.png')