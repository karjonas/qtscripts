import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
gradient = np.linspace(0, 1, 256)

for cm in ['rainbow', 'viridis', 'coolwarm', 'gist_rainbow', 'plasma', 'gnuplot']:
    mpl.pyplot.imsave("colormap-"+cm+".png", [gradient], cmap=cm)