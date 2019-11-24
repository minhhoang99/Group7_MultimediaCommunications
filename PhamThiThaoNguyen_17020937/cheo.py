import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib
listColorOfRainbow = [
    "#ff0000",
    "#ff7f00",
    "#ffff00",
    "#00ff00",
    "#0000ff",
    "#4B0082",
    "#9400D3"
]

my_map = cm.get_cmap("Spectral")

c = np.outer(np.arange(0,1,0.01),np.ones(10))

colors = [my_map(i) for i in np.linspace(0, 1, len(c))]
sm = plt.cm.ScalarMappable(cmap=my_map, norm=plt.Normalize(np.min(c),np.max(c)))
sm._A = []

fig = plt.figure()
ax1 = fig.add_subplot(211)

for i in range(len(c)):
    c0 = c[i]
    ax1.plot(c+c0,c,color=colors[i])
#
# for i in range(len(c)):
#     c0 = c[i]
#     ax1.plot(c-0.6*c0,c-0.6*c0, color=colors[i])

plt.savefig('cheo.png')

