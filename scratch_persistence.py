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


d = 1



P1 = np.loadtxt('/Users/sinanunver/Desktop/xy-of-boundary-points/aorta01_91_bnd.txt', delimiter=',')
P2 = np.loadtxt('/Users/sinanunver/Desktop/xy-of-boundary-points/aorta01_127_bnd.txt', delimiter=',')


plt.subplot(1, 2, 1)
plt.scatter(P1[:,0],P1[:,1], label = 'P1')
plt.subplot(1, 2, 2)
plt.scatter(P2[:,0],P2[:,1], label = 'P2')
plt.show()




# Compute their diagrams
diagrams1 = ripser.ripser(P1)['dgms']
diagrams2 = ripser.ripser(P2)['dgms']

distance_bottleneck, matching = persim.bottleneck(diagrams1[d], diagrams2[d], matching=True)

plt.subplot(1, 3, 1)
Draw.drawDgm(diagrams1[d])


plt.subplot(1, 3, 2)
Draw.drawDgm(diagrams2[d])

plt.subplot(1, 3, 3)
persim.bottleneck_matching(diagrams1[d], diagrams2[d], matching, labels=['diag1', 'diag2'])

plt.show()



# # Compute bottleneck distance using scikit-tda

# print('The bottleneck distance between diagram 1 and 2 is', distance_bottleneck)

print(distance_bottleneck)
print(matching)


