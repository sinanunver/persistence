# This code below reads from '.../xy-of-boundary-points/...' and '.../res/res1a/...'
# to find the 5 maximum bottleneck distances and then plot the corresponding persistence
# diagrams. These are only done for dim 0 and only for the image 1. I changed this 9 times
# to get the data for the other images. It is probably better to do a for loop for this.
# I copied the code and did the same for dim 1 homology. This can also be simultaneously did with a
# loop.


import matplotlib.pyplot as plt
import os
import re
import numpy as np
import ripser
import persim
import sys
import teaspoon.TDA.Draw as Draw



def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)


# This function finds the maximum N values in a list. This is used to find the largest
# 5 bottleneck distances between consecutive images of a patient.

def Nmaxelements(list1, N):
    final_list = []


    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    return final_list

path = '/Users/sinanunver/OneDrive - Koc Universitesi/DeepLearning/aort/xy-of-boundary-points/1'

files = os.listdir(path)
sorted_files = sorted_alphanumeric(files)

pa = []
for line in open('/Users/sinanunver/Desktop/res/res1a.txt', 'r'):
    pa.append(line)
pfa = [float(x) for x in pa]

# A copy is used since the for loop below seems to change the file.

pfa_copy = pfa.copy()


pb = []
for line in open('/Users/sinanunver/Desktop/res/res1b.txt', 'r'):
    pb.append(line)
pfb = [float(x) for x in pb]


# A copy is used since the for loop below seems to change the file.

pfb_copy = pfb.copy()

plt.plot(pfa)
plt.plot(pfb)
plt.show()



pfa_5 = Nmaxelements(pfa_copy, 5)
pfb_5 = Nmaxelements(pfb_copy, 5)





ind_pfa_5 = [i for i, x in enumerate(pfa) if x in pfa_5]
ind_pfb_5 = [i for i, x in enumerate(pfb) if x in pfb_5]


# The loop below re-plots the maximum distance images, their persistence diagrams and
# the matching between the persistence diagrams that give the bottleneck distance. These
# are all done only for dim 0 persistence.

for i in range(5):
    file1 = sorted_files[ind_pfa_5[i]]
    file2 = sorted_files[ind_pfa_5[i]+1]
    current1 = os.path.join(path, file1)
    current2 = os.path.join(path, file2)
    P1 = np.loadtxt(current1, delimiter=',')
    P2 = np.loadtxt(current2, delimiter=',')
    diagrams1 = ripser.ripser(P1)['dgms']
    diagrams2 = ripser.ripser(P2)['dgms']
    distance_bottleneck, matching = persim.bottleneck(diagrams1[0], diagrams2[0], matching=True)
    print('The bottleneck distance between diagram ' + current1 + ' and ' + current2 + ' is', distance_bottleneck)
    plt.subplot(1, 2, 1)
    plt.scatter(P1[:, 0], P1[:, 1], label='P1')
    plt.subplot(1, 2, 2)
    plt.scatter(P2[:, 0], P2[:, 1], label='P2')
    plt.show()
    plt.subplot(1, 3, 1)
    Draw.drawDgm(diagrams1[0])

    plt.subplot(1, 3, 2)
    Draw.drawDgm(diagrams2[0])

    plt.subplot(1, 3, 3)
    persim.bottleneck_matching(diagrams1[0], diagrams2[0], matching, labels=['diag1', 'diag2'])

    plt.show()

