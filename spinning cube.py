import matplotlib
# Set the backend (use 'Qt5Agg', 'TkAgg', or another if you're aware of what's available on your system)
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vertices = np.array([[-1, -1, -1],
                     [1, -1, -1 ],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1 ],
                     [1, 1, 1],
                     [-1, 1, 1]])


edges = [[vertices[n] for n in face] for face in 
         [(0,1,5,4), (7,6,2,3), (0,3,7,4), (1,2,6,5)]]

faces = Poly3DCollection(edges, linewidths=1, edgecolors='k', alpha=.25)
ax.add_collection3d(faces)


edges_collection = Line3DCollection(edges, colors='k', linewidths=0.5, linestyles=':', alpha=0.4)
ax.add_collection3d(edges_collection)


ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.axis('off') 


def animate(i):
    ax.view_init(elev=10., azim=i)


ani = FuncAnimation(fig, animate, frames=np.arange(0, 360, 1), interval=10, blit=False)


plt.show()


ani.save('spinning_cube.gif', writer='pillow')