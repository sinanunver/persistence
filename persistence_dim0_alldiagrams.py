import matplotlib.pyplot as plt
import os
import re
import numpy as np
import ripser
import persim
import sys
import teaspoon.TDA.Draw as Draw
import shutil


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)


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

# file_a = open('/Users/sinanunver/Desktop/bottleneck_dim0_max5.txt', 'w')
for x in range(10):
    y = x+1

    path = '/Users/sinanunver/OneDrive - Koc Universitesi/DeepLearning/aort/xy-of-boundary-points/' + str(y)
    path_image = '/Users/sinanunver/OneDrive - Koc Universitesi/DeepLearning/aort/images-of-boundary-points/'

    files = os.listdir(path)
    sorted_files = sorted_alphanumeric(files)

    pa = []
    for line in open('/Users/sinanunver/Desktop/res/res' +str(y) +'a.txt', 'r'):
        pa.append(line)

    pfa = [float(x) for x in pa]

    pfa_copy = pfa.copy()


    pb = []
    for line in open('/Users/sinanunver/Desktop/res/res'+str(y)+'b.txt', 'r'):
        pb.append(line)
    pfb = [float(x) for x in pb]

    pfb_copy = pfb.copy()

    plt.plot(pfa)
    plt.plot(pfb)
    # plt.suptitle('Aort ' + str(y) + '-dim 0 homology')
    # plt.show()


    pfa_5 = Nmaxelements(pfa_copy, 5)
    pfb_5 = Nmaxelements(pfb_copy, 5)





    ind_pfa_5 = [i for i, x in enumerate(pfa) if x in pfa_5]
    ind_pfb_5 = [i for i, x in enumerate(pfb) if x in pfb_5]


    for i in range(5):
        j = i + 1
        file_scatter = 'figures-dim0_' + str(y) + '_scatter' + str(j) + '.png'
        file_bottleneck = 'figures-dim0_' + str(y) + '_bottleneck' + str(j) + '.png'
        file1 = sorted_files[ind_pfa_5[i]]
        file2 = sorted_files[ind_pfa_5[i]+1]
        current1 = os.path.join(path, file1)
        current2 = os.path.join(path, file2)
        current1_image = os.path.join(path_image, file1).replace('txt', 'png')
        current2_image = os.path.join(path_image, file2).replace('txt', 'png')
        shutil.copy(current1_image, '/Users/sinanunver/Desktop/dim0-max5/' + str(j))
        shutil.copy(current2_image, '/Users/sinanunver/Desktop/dim0-max5/' + str(j))
        P1 = np.loadtxt(current1, delimiter=',')
        P2 = np.loadtxt(current2, delimiter=',')
        diagrams1 = ripser.ripser(P1)['dgms']
        diagrams2 = ripser.ripser(P2)['dgms']
        distance_bottleneck, matching = persim.bottleneck(diagrams1[0], diagrams2[0], matching=True)
        current1_short = current1.replace('/Users/sinanunver/OneDrive - Koc Universitesi/DeepLearning/aort/xy-of-boundary-points', '').replace(
            '_bnd.txt', '').replace('/','').replace('aorta','')
        current2_short = current2.replace(
            '/Users/sinanunver/OneDrive - Koc Universitesi/DeepLearning/aort/xy-of-boundary-points', '').replace(
            '_bnd.txt', '').replace('/','').replace('aorta','')
        # print('The dim 0 bottleneck distance between diagram ' + current1_short +
        #       ' and ' + current2_short + ' is', distance_bottleneck)
        plt.subplot(1, 2, 1)
        plt.scatter(P1[:, 0], P1[:, 1], label='P1')
        plt.subplot(1, 2, 2)
        plt.scatter(P2[:, 0], P2[:, 1], label='P2')
        plt.suptitle(current1_short + ' and ' + current2_short)
        # plt.savefig(file_scatter)
        # plt.show()
        plt.subplot(1, 3, 1)
        Draw.drawDgm(diagrams1[0])

        plt.subplot(1, 3, 2)
        Draw.drawDgm(diagrams2[0])

        plt.subplot(1, 3, 3)
        persim.bottleneck_matching(diagrams1[0], diagrams2[0], matching, labels=['diag1', 'diag2'])
        plt.suptitle(current1_short + ' and ' + current2_short)
        # plt.savefig(file_bottleneck)
        # plt.show()
        # file_a.write('The dim 0 bottleneck distance between diagram ' + current1_short +
        #       ' and ' + current2_short + ' is '+str(distance_bottleneck) + '\n')
# file_a.close()