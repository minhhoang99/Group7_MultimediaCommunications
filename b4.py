

import scipy.fftpack as sf
import numpy as np
import matplotlib.pyplot as plt
#astype(float) chuyển đổi về kiểu float
im = plt.imread('face.png').astype(float)
#xem ảnh gốc
	# plt.figure()
	# plt.imshow(im, plt.cm.gray)
	# plt.title('anh_goc')

#tần số của ảnh

im_fft = sf.fft2(im)

def plot_spectrum(img_fft):
    from matplotlib.colors import LogNorm
    # A logarithmic colormap
    plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5))
    plt.colorbar()

plt.figure()
plot_spectrum(im_fft)
plt.savefig("face_for.jpg")
plt.title('Fourier transform')

#khôi phục ảnh
im_fft2 = im_fft.copy()
im_new = sf.ifft2(im_fft2).real

plt.figure()
plt.imshow(im_new, plt.cm.gray)
plt.title('Reconstructed Image')

plt.show()