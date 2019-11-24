1.
numpy.convolve(a, v, mode='full')[source]
Returns the discrete, linear convolution of two one-dimensional sequences.
By default, mode is ‘full’. This returns the convolution at each point of overlap, with an output shape of (N+M-1,). At the end-points of the convolution, the signals do not overlap completely, and boundary effects may be seen.