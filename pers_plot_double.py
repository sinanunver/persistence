import matplotlib.pyplot as plt




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







            plt.subplot(2, 1, 1)
            plt.suptitle('dim 0 and dim 1 persistence for no ' + str(w) + ' and ' + str(t))
            plt.plot(len_a, pfa)
            plt.plot(len_a2, pfa2)



            plt.subplot(2, 1, 2)
            plt.plot(len_b, pfb)
            plt.plot(len_b2, pfb2)


            bottleneck_plot_double = 'bottleneck plot' + str(w) +' and '+ str(t) + '.png'
            plt.savefig(bottleneck_plot_double)
            plt.show()



