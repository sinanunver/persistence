# Basic imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import networkx as nx
from IPython.display import Video

# scikit-tda imports..... Install all with -> pip install scikit-tda
#--- this is the main persistence computation workhorse
import ripser
# from persim import plot_diagrams
import persim
# import persim.plot

# teaspoon imports...... Install with -> pip install teaspoon
#---these are for generating data and some drawing tools
import teaspoon.MakeData.PointCloud as makePtCloud
import teaspoon.TDA.Draw as Draw

#---these are for generating time series network examples
from networkx.algorithms import matching
from teaspoon.SP.network import ordinal_partition_graph
from teaspoon.TDA.PHN import PH_network
from teaspoon.SP.network_tools import make_network
from teaspoon.parameter_selection.MsPE import MsPE_tau
import teaspoon.MakeData.DynSysLib.DynSysLib as DSL


def DoubleAnnulus(r1 = 1, R1 = 2, r2 = .8, R2 = 1.3, xshift = 3):
    P = makePtCloud.Annulus(r = r1, R = R1)
    Q = makePtCloud.Annulus(r = r2, R = R2)
    Q[:,0] = Q[:,0] + xshift
    P = np.concatenate((P, Q) )
    return(P)


# Make three example point clouds
r = 1
R = 2
P1 = makePtCloud.Annulus(N=200, r=r, R=R, seed=None) # teaspoon data generation
P2 = makePtCloud.Annulus(N=200, r=r, R=R, seed=None)
P2[:,1] += 6
P3 = DoubleAnnulus()
P3 *= 1.1
P3[:,0] += 6
P3[:,1] += 3

# plt.figure(figsize = (15,5))
plt.scatter(P1[:,0],P1[:,1], label = 'P1')
#plt.show()
plt.scatter(P2[:,0],P2[:,1], label = 'P2')
#plt.show()
plt.scatter(P3[:,0],P3[:,1], label = 'P3')
plt.axis('equal')
plt.legend
plt.show()

# Compute their diagrams
diagrams1 = ripser.ripser(P1)['dgms']
diagrams2 = ripser.ripser(P2)['dgms']
diagrams3 = ripser.ripser(P3)['dgms']


fig, axes = plt.subplots(nrows=1, ncols=3, figsize = (20,5))
plt.sca(axes[0])

Draw.drawDgm(diagrams1[1])

plt.sca(axes[1])
Draw.drawDgm(diagrams2[1])
plt.sca(axes[2])
Draw.drawDgm(diagrams3[1])
plt.show()

# Compute bottleneck distance using scikit-tda
distance_bottleneck, matching = persim.bottleneck(diagrams1[1], diagrams2[1], matching=True)
persim.bottleneck_matching(diagrams1[1], diagrams2[1], matching, labels=['diag1', 'diag2'])
print('The bottleneck distance between diagram 1 and 2 is', distance_bottleneck)
plt.show()
# print(matching)
# print(D)

# Compute bottleneck distance using scikit-tda
distance_bottleneck, matching = persim.bottleneck(diagrams1[1], diagrams3[1], matching=True)
persim.bottleneck_matching(diagrams1[1], diagrams3[1], matching, labels=['diag1', 'diag3'])
print('The bottleneck distance between diagram 1 and 3 is', distance_bottleneck)
plt.show()

# print(matching)
# print(D)

