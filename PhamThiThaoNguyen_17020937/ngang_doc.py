from matplotlib import pyplot as plt
import matplotlib
import numpy as np


a = np.outer(np.arange(0,1,0.01),np.ones(10))
listColorOfRainbow = [
    "#ff0000",
    "#ff7f00",
    "#ffff00",
    "#00ff00",
    "#0000ff",
    "#4B0082",
    "#9400D3"
]

fig, ax = plt.subplots()
cax = fig.add_axes([0.2, 0.8, 0.5, 0.05])
my_cmap2 = matplotlib.colors.LinearSegmentedColormap.from_list('rainbow', listColorOfRainbow, N = 256)


im = ax.imshow(a,aspect='auto', cmap = my_cmap2)
fig.colorbar(im, cax=cax, orientation='horizontal')
plt.savefig('ngang_doc.png')


