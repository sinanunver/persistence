# This code makes a graph of all the bottleneck distances for dim 0 and dim 1 for a
#     particular patient. The largest five distances are marked with an 'x'

import matplotlib.pyplot as plt


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


for w in range(1,11):


    pa = []
    for line in open('/Users/sinanunver/Desktop/res/res'+str(w) +'a.txt', 'r'):
        pa.append(line)
    pfa = [float(x) for x in pa]

    len_a = list(range(0, len(pfa)))

    pb = []
    for line in open('/Users/sinanunver/Desktop/res/res'+str(w)+'b.txt', 'r'):
        pb.append(line)
    pfb = [float(x) for x in pb]

    len_b = list(range(0, len(pfb)))

    pfa_copy = pfa.copy()
    pfb_copy = pfb.copy()

    pfa_5 = Nmaxelements(pfa_copy, 5)
    pfb_5 = Nmaxelements(pfb_copy, 5)

    ind_a = [i for i, x in enumerate(pfa) if x in pfa_5]

    pfa5_reorder = [pfa[j] for j in ind_a]

    ind_b = [i for i, x in enumerate(pfb) if x in pfb_5]

    pfb5_reorder = [pfb[j] for j in ind_b]

    plt.subplot(2, 1, 1)
    plt.suptitle('dim 0 and dim 1 persistence for no ' + str(w))
    plt.scatter(len_a, pfa)
    for i in range(5):
        plt.annotate('x', (ind_a[i], pfa5_reorder[i]))
    plt.subplot(2, 1, 2)
    plt.scatter(len_b, pfb)
    for i in range(5):
        plt.annotate('x', (ind_b[i], pfb5_reorder[i]))
    bottleneck_scatter = 'bottleneck scatter' + str(w) + '.png'
    # plt.savefig(bottleneck_scatter)
    plt.show()


