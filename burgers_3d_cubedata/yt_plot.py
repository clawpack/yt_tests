
import yt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from clawpack.pyclaw import Solution
import numpy as np
import matplotlib.pyplot as plt

from clawpack.pyclaw import Solution

frame = 1
def load_yt(frame):

    sol = Solution(frame,path='_output',file_format='ascii')

    grid_data = []
     
    for state in sorted(sol.states, key = lambda a: a.patch.level):
        patch = state.patch
        d = {
            'left_edge': patch.lower_global,
            'right_edge': patch.upper_global,
            'level': patch.level,
            'dimensions': patch.num_cells_global,
            'q': state.q[0,...],
            'number_of_particles': 0,
            }
        grid_data.append(d)

    ds = yt.load_amr_grids(grid_data, sol.patch.num_cells_global)
    return ds

ds = load_yt(frame)

#s = ds.slice(1, 0.) # normal to  y axis at y=0
s = ds.slice(0, 0.6) # normal to x axis at x=0.6
width = (3,'cm')
res = [400,400]
frb = s.to_frb(width,res)
q = np.array(frb['q'])

plt.clf()
plt.imshow(q)
plt.contour(q,10,colors='w')
plt.show()
