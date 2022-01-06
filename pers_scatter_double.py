# This code gives a plot of dim 0 and dim 1 bottlenecks for two figures at the same time in scatter form. The answer is
#     written on bottleneck_scatter_double file. The largest 5 distances are marked with an 'x'

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
    for t in range(1,11):
        if w < t:
            pa = []
            for line in open('/Users/sinanunver/Desktop/res/res' + str(w) + 'a.txt', 'r'):
                pa.append(line)
            pfa = [float(x) for x in pa]
            len_a = list(range(0, len(pfa)))

            pa2 = []
            for line in open('/Users/sinanunver/Desktop/res/res' + str(t) + 'a.txt', 'r'):
                pa2.append(line)
            pfa2 = [float(x) for x in pa2]
            len_a2 = list(range(0, len(pfa2)))


            pb = []
            for line in open('/Users/sinanunver/Desktop/res/res' + str(w) + 'b.txt', 'r'):
                pb.append(line)
            pfb = [float(x) for x in pb]
            len_b = list(range(0, len(pfb)))

            pb2 = []
            for line in open('/Users/sinanunver/Desktop/res/res' + str(t) + 'b.txt', 'r'):
                pb2.append(line)
            pfb2 = [float(x) for x in pb2]
            len_b2 = list(range(0, len(pfb2)))


            pfa_copy = pfa.copy()
            pfa_copy2 = pfa2.copy()

            pfb_copy = pfb.copy()
            pfb_copy2 = pfb2.copy()

            pfa_5 = Nmaxelements(pfa_copy, 5)
            pfa_52 = Nmaxelements(pfa_copy2, 5)

            pfb_5 = Nmaxelements(pfb_copy, 5)
            pfb_52 = Nmaxelements(pfb_copy2, 5)

            ind_a = [i for i, x in enumerate(pfa) if x in pfa_5]
            ind_a2 = [i for i, x in enumerate(pfa2) if x in pfa_52]

            pfa5_reorder = [pfa[j] for j in ind_a]
            pfa5_reorder2 = [pfa2[j] for j in ind_a2]

            ind_b = [i for i, x in enumerate(pfb) if x in pfb_5]
            ind_b2 = [i for i, x in enumerate(pfb2) if x in pfb_52]

            pfb5_reorder = [pfb[j] for j in ind_b]
            pfb5_reorder2 = [pfb2[j] for j in ind_b2]

            plt.subplot(2, 1, 1)
            plt.suptitle('dim 0 and dim 1 persistence for no ' + str(w) + ' and ' + str(t))
            plt.scatter(len_a, pfa)
            for i in range(5):
                plt.annotate('x', (ind_a[i], pfa5_reorder[i]))
            plt.scatter(len_a2, pfa2)
            for i in range(5):
                plt.annotate('x', (ind_a2[i], pfa5_reorder2[i]))



            plt.subplot(2, 1, 2)
            plt.scatter(len_b, pfb)
            for i in range(5):
                plt.annotate('x', (ind_b[i], pfb5_reorder[i]))
            plt.scatter(len_b2, pfb2)
            for i in range(5):
                plt.annotate('x', (ind_b2[i], pfb5_reorder2[i]))

            # bottleneck_scatter_double = 'bottleneck scatter' + str(w) +' and '+ str(t) + '.png'
            # plt.savefig(bottleneck_scatter_double)
            plt.show()



