import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from joblib import Parallel, delayed
import time


import queue # imported for using queue.Empty exception
from matplotlib.colors import LogNorm

SENTINEL = None

def function(c):
    z = complex(0, 0) + c
    nz = complex
    counter = 1

    while (abs(z) < 2) and (counter < 1000):
        nz = z ** 2 + c
        z = nz
        counter += 1

    return counter - np.log(np.log(2) / np.log(4)) / np.log(2)


center_y = -0.318
center_x = -1.20608

#for x in range(1, 50):
def start(x):
    print(x)
    l = []
    a = 2.0 / 3**x
    start_x = center_x - a
    end_x = center_x + a
    start_y = center_y - a
    end_y = center_y + a

    resolution_x = 1000
    resolution_y = 1000

    # step_size_y = (end_y - start_y) / resolution_y
    # step_size_x = (end_x - start_x) / resolution_x

    for i in np.linspace(start_x, end_x, resolution_x, endpoint=True):
        for y in np.linspace(start_y, end_y, resolution_y, endpoint=True):
            go = function(complex(i, y))
            ll = [i, y, go]
            l.append(ll)

    l = np.array(l)

    z = l[:, 2]

    N = int(len(z) ** .5)
    z = z.reshape(N, N)
    plt.imshow(z, extent=(np.amin(l[:, 1]), np.amax(l[:, 1]), np.amin(l[:, 0]), np.amax(l[:, 0])),
               cmap=cm.hot, norm=mpl.colors.Normalize(vmin=-0, vmax=100))
    plt.savefig(str(x) + '.jpg', dpi=1000)

    # plt.show()
    # print(function(complex(-1.2000000000000002, -4.440892098500626e-16)))


if __name__ == "__main__":
    num_steps = 100.0
    Parallel(n_jobs=20)(delayed(start)(x) for x in np.linspace(1.0, num_steps, int(num_steps), endpoint=True))


