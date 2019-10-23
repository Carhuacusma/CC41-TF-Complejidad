#!/usr/bin/env python
# coding: utf-8

# In[63]:


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt

points = np.array([[0, 0, 0],
                  [0, 0,  4],#0
                  [4, 0, 4],
                  [4, 0, 0],#0
                  [0, 4, 0],
                  [0, 4, 4],#0
                  [4, 4, 4],
                  [4, 4, 0]])

P = [[1 , 1 ,  1],
 [1 ,  1 ,  1],
 [1 ,  1 , 1]]

Z = points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax2= fig.add_subplot(111, projection='3d')

r = [0,0]

X, Y = np.meshgrid(r, r)
# plot vertices
ax.scatter3D(Z[:, 0], Z[:, 1],Z[:, 2])
print(Z[:, 0], Z[:, 1],Z[:, 2])

# list of sides' polygons of figure
verts = [[Z[0],Z[1],Z[2],Z[3]],
         [Z[4],Z[5],Z[6],Z[7]], 
         [Z[0],Z[1],Z[5],Z[4]], 
         [Z[2],Z[3],Z[7],Z[6]], 
         [Z[1],Z[2],Z[6],Z[5]],
         [Z[4],Z[7],Z[3],Z[0]]]

verts2 = [[Z[0]+10,Z[1]+10,Z[2]+10,Z[3]+10],
         [Z[4]+10,Z[5]+10,Z[6]+10,Z[7]+10], 
         [Z[0]+10,Z[1]+10,Z[5]+10,Z[4]+10], 
         [Z[2]+10,Z[3]+10,Z[7]+10,Z[6]+10], 
         [Z[1]+10,Z[2]+10,Z[6]+10,Z[5]+10],
         [Z[4]+10,Z[7]+10,Z[3]+10,Z[0]+10]]
# plot sides
ax.add_collection3d(Poly3DCollection(verts2, 
 facecolors = 'cyan', linewidths=1, edgecolors='y', alpha=.5))

ax.add_collection3d(Poly3DCollection(verts, 
 facecolors = 'red', linewidths=1, edgecolors='r', alpha=.5))

#ax2.add_collection3d(Poly3DCollection(verts2, 
 #facecolors = 'cyan', linewidths=1, edgecolors='r', alpha=.25))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

