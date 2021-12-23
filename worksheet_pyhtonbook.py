import numpy as np
import persim
import tadasets
import ripser
import matplotlib.pyplot as plt

data_clean = tadasets.dsphere(d=1, n=100, noise=0.0)
data_noisy = tadasets.dsphere(d=1, n=100, noise=0.1)

plt.scatter(data_clean[:,0], data_clean[:,1], label="clean data")
plt.scatter(data_noisy[:,0], data_noisy[:,1], label="noisy data")
plt.axis('equal')
plt.legend()
plt.show()

dgm_clean = ripser.ripser(data_clean)['dgms'][1]
dgm_noisy = ripser.ripser(data_noisy)['dgms'][1]

persim.plot_diagrams([dgm_clean, dgm_noisy] , labels=['Clean $H_1$', 'Noisy $H_1$'])
plt.show()

distance_bottleneck, matching = persim.bottleneck(dgm_clean, dgm_noisy, matching=True)

persim.bottleneck_matching(dgm_clean, dgm_noisy, matching, labels=['Clean $H_1$', 'Noisy $H_1$'])
plt.show()

print(distance_bottleneck)
persim.bottleneck(dgm_clean, dgm_noisy)

dgm1 = np.array([
    [0.6, 1.05],
    [0.53, 1],
    [0.5, 0.51]
])
dgm2 = np.array([
    [0.55, 1.1],
    [0.8,0.9]
])

d, matching = persim.bottleneck(
    dgm1,
    dgm2,
    matching=True
)

persim.bottleneck_matching(dgm1, dgm2, matching, labels=['Clean $H_1$', 'Noisy $H_1$'])
plt.title("Distance {:.3f}".format(d))
plt.show()


