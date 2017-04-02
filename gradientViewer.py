"""
Jhonatan da Silva
Last Updated version :
Sun Apr  2 17:59:33 2017
Number of code lines: 
70
"""
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

def createMesh(xRange,yRange):
    mesh = []
    xRange += 1
    yRange += 1
    for i in range(xRange):
        for j in range(yRange):
            mesh.append([i,j])
            mesh.append([-i,j])
            mesh.append([i,-j])
            mesh.append([-i,-j])
    return mesh

fig = plt.figure()
j = 0
ax = plt.axes()
ax.set_ylim([-10,10])
ax.set_xlim([-10,10])
points = createMesh(10,10)

def F(values):
    x = values[0]
    y = values[1]
    fx = -y
    fy = x

    return [x,y,fx,fy]

def norma(vec):
    x = vec[2] - vec[0]
    y = vec[3] - vec[1]
    return np.sqrt(x**2 + y**2)

def livePlot(i):
    #    for p in points:
    global j 
    ax.set_ylim([-10,10])
    ax.set_xlim([-10,10])
    maxValue = len(points) - 1
    p = F(points[j])
    n = norma(p)
    if n < 4:
        color = "Red"
    elif n >= 4 and n < 8:
        color = "Blue"
    elif n >= 8 and n < 12:
        color = "Teal"
    else:
        color = "Green"
    plt.quiver(p[0],p[1],p[2],p[3],headlength=4,\
               edgecolor='k',linewidth=.5,\
               alpha=0.5,color=color)
    plt.scatter(p[0],p[1],color='k',s=10)
    if j == maxValue:
        j = 0
        ax.clear()
        ax.set_ylim([-10,10])
        ax.set_xlim([-10,10])
    j+=1

def makeAnimation():
    a = animation.FuncAnimation(fig,livePlot,interval=1e-10)
    plt.show()

makeAnimation()
