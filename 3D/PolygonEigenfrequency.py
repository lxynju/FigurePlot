# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:01:29 2023

@author: dell
"""

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
plt.rcParams['font.size'] = 18
#ax.view_init(elev=0, azim=-90, roll=0)

colors = ['r', 'g', 'b']
radial = [2, 1, 0]

for c, m in zip(colors,radial):
    l = np.arange(0,9)
    omega = np.sqrt(2)*np.sqrt(2*m**2 + 2*m*l + 2*m + l)
    
    cs = [c] * len(l)
    
    ax.bar(l, omega, m, zdir ='y', color=cs, alpha = 0.8)
    
ax.set_xlabel('$l$')
ax.set_ylabel('$m$')
ax.set_zlabel('$\omega_{m,l}$')

#ax.set_xticks(l)
ax.set_yticks(radial)
#ax.set_yticks([])
ax.set_zticks([0,2,4,6,8,10])

plt.show

