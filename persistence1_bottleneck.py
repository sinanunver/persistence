# Here we collect data from '.../xy-of-boundary-points/...' and write the bottleneck
# distances of the persistence diagrams of the consecutive images in the file. For example
# for image 1, we write the  one for dim 0 to the file .../res1a/... and the dimension 1 to
# .../res1b/... Rather than doing a for loop for 10x2=20 I had to run the program 20 times
# changing the file names by hand. We do not consider homology of degree greater than 1.


import numpy as np
import ripser
import persim
import os
import sys
import re

# This function is for sorting the names of the images so we get the consecutive images for the
# same patient.

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)



d = 1

path = '/Users/sinanunver/OneDrive - Koc Universitesi/DeepLearning/aort/xy-of-boundary-points/10'

files = os.listdir(path)

sorted_files = sorted_alphanumeric(files)



fid = open('/Users/sinanunver/Desktop/res/res10b.txt', 'w')
for i in range(33):
    file1 = sorted_files[i]
    file2 = sorted_files[i+1]
    current1 = os.path.join(path, file1)
    current2 = os.path.join(path, file2)
    P1 = np.loadtxt(current1, delimiter=',')
    P2 = np.loadtxt(current2, delimiter=',')
    diagrams1 = ripser.ripser(P1)['dgms']
    diagrams2 = ripser.ripser(P2)['dgms']
    distance_bottleneck, matching = persim.bottleneck(diagrams1[d], diagrams2[d], matching=True)
    # # print('The bottleneck distance between diagram ' + current1.replace("_bnd.txt", "").replace(
    #     "/Users/sinanunver/Desktop/xy-of-boundary-points/aorta01_", "") + ' and ' + current2.replace("_bnd.txt",
    #                                                                                                 "").replace(
    #     "/Users/sinanunver/Desktop/xy-of-boundary-points/aorta01_", "") + ' is', distance_bottleneck)

    fid.write(str(distance_bottleneck) + '\n')

fid.close()