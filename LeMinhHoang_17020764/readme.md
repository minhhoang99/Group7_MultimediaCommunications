## **Libraries and function used:**
**1, numpy.convolve(a, v, mode)**
[source]: [https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html]

Returns the discrete, linear convolution of two one-dimensional sequences.

The convolution operator is often seen in signal processing, where it models the effect of a linear time-invariant system on a signal [1]. In probability theory, the sum of two independent random variables is distributed according to the convolution of their individual distributions. At the end-points of the convolution, the signals do not overlap completely, and boundary effects may be seen.

**2, numpy.argmax(a, axis=None, out=None)**
[source] : https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html

Returns the indices of the maximum values along an axis.

**3, numpy.argmax(a, axis=None, out=None)**
[source] : https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmin.html#numpy.argmin

Returns the indices of the minimum values along an axis.

**4, numpy.zeros(shape, dtype=float, order='C')**

Return a new array of given shape and type, filled with zeros.

**5, numpy.dot(a, b, out=None)**
[https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html]

Dot product of two arrays.

**6, numpy.fft.fft(a, n=None, axis=-1, norm=None)**
[https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html]

Compute the one-dimensional discrete Fourier Transform.

This function computes the one-dimensional n-point discrete Fourier Transform (DFT) with the efficient Fast Fourier Transform (FFT) algorithm [CT].

**7, numpy.fft.ifft(a, n=None, axis=-1, norm=None)**
[https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifft.html]

Compute the one-dimensional inverse discrete Fourier Transform.

This function computes the inverse of the one-dimensional n-point discrete Fourier transform computed by fft. In other words, ifft(fft(a)) == a to within numerical accuracy. For a general description of the algorithm and definitions, see numpy.fft.

The input should be ordered in the same way as is returned by fft, i.e.,

a[0] should contain the zero frequency term,
a[1:n//2] should contain the positive-frequency terms,
a[n//2 + 1:] should contain the negative-frequency terms, in increasing order starting from the most negative frequency.
For an even number of input points, A[n//2] represents the sum of the values at the positive and negative Nyquist frequencies, as the two are aliased together. See numpy.fft for details.

**8,numpy.pad(array, pad_width, mode='constant', **kwargs)**
[https://docs.scipy.org/doc/numpy/reference/generated/numpy.pad.html]

Pad an array.

**9, numpy.hstack(tup)**
[https://docs.scipy.org/doc/numpy/reference/generated/numpy.hstack.html]

Stack arrays in sequence horizontally (column wise).

This is equivalent to concatenation along the second axis, except for 1-D arrays where it concatenates along the first axis. Rebuilds arrays divided by hsplit.

This function makes most sense for arrays with up to 3 dimensions. For instance, for pixel-data with a height (first axis), width (second axis), and r/g/b channels (third axis). The functions concatenate, stack and block provide more general stacking and concatenation operations.

**10, numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)**
[https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html]

Returns True if two arrays are element-wise equal within a tolerance.

The tolerance values are positive, typically very small numbers. The relative difference (rtol * abs(b)) and the absolute difference atol are added together to compare against the absolute difference between a and b.

If either array contains one or more NaNs, False is returned. Infs are treated as equal if they are in the same place and of the same sign in both arrays.

**11, numpy.in1d(ar1, ar2, assume_unique=False, invert=False)**
[https://docs.scipy.org/doc/numpy/reference/generated/numpy.in1d.html]

Test whether each element of a 1-D array is also present in a second array.

Returns a boolean array the same length as ar1 that is True where an element of ar1 is in ar2 and False otherwise.

We recommend using isin instead of in1d for new code.