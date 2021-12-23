import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import networkx as nx
import ripser
import persim
import os
import sys
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)


# P1 = np.loadtxt('/Users/sinanunver/Desktop/xy-of-boundary-points/aorta01_43_bnd.txt', delimiter=',')
#
# diagrams1 = ripser.ripser(P1)['dgms']

path = '/Users/sinanunver/Desktop/xy-of-boundary-points'

files = os.listdir(path)

sorted_files = sorted_alphanumeric(files)


for file in sorted_files:
    current0 = os.path.join(path, file)
    if os.path.isfile(current0):
        P1 = np.loadtxt(current0,delimiter=',')
        diagrams1 = ripser.ripser(P1)['dgms']

        for file in sorted_files:
            current = os.path.join(path, file)
            if os.path.isfile(current):
                P2 = np.loadtxt(current,delimiter=',')
                diagrams2 = ripser.ripser(P2)['dgms']
                distance_bottleneck, matching = persim.bottleneck(diagrams1[1], diagrams2[1], matching=True)
                print('The bottleneck distance between diagram '+ current0.replace("_bnd.txt","").replace("/Users/sinanunver/Desktop/xy-of-boundary-points/aorta01_","")  +' and '+ current.replace("_bnd.txt","").replace("/Users/sinanunver/Desktop/xy-of-boundary-points/aorta01_","")+' is', distance_bottleneck)