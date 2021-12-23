import cv2
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
import persim
import tadasets
import ripser
import matplotlib.pyplot as plt

import geek


img1 = cv2.imread('/Users/sinanunver/Desktop/27.jpg', 0)



g_f = np.asarray(img1, dtype=float)
#plt.imshow(g1,cmap='gray')
#plt.show()

g = np.asarray(img1)

print(g.shape)


g_flat=np.sort(g_f.flatten())


print(st.mean(g_flat))

print(st.mode(g_flat))

print(st.median(g_flat))

k=180

gnew=g
for i in range(480):
      for j in range(640):

        if (gnew[i,j]<=k):
           gnew[i,j] = 0
        else:
           gnew[i,j] = 255


plt.imshow(gnew, cmap='gray')
plt.show()

#g2 = np.asarray(img2)
#plt.imshow(g2,cmap='gray')
#plt.show()

#gmax=np.maximum(g1,g2)
#plt.imshow(gmax,cmap='gray')
#plt.show()

#gmin=np.minimum(g1,g2)
#plt.imshow(gmin,cmap='gray')
#plt.show()

#dgms = ripser.ripser(gnew)['dgms']
#ripser.plot_diagrams(dgms, show=True)

an_array = np.transpose(np.nonzero(gnew))


list=[]

for i in range(610):
    list.append(str(an_array[i,0])+", "+str(an_array[i,1]))


#print(list)



with open('../../Library/Application Support/JetBrains/PyCharmCE2021.2/scratches/listfile.txt', 'w') as filehandle:
    for listitem in list:
        filehandle.write('%s\n' % listitem)


#a_file = open("test.txt", "w")
#for a in list:
#    np.savetxt(a_file, a)

#a_file.close()


#data = []
#with open('test.txt') as my_file:
#    for line in my_file:
#        data.append([list(map(float ,x.split(','))) for x in line.split(' ')])
#print(my_file)