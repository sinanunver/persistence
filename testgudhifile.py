import numpy as np
from gudhi.representations import Landscape
# A single diagram with 4 points
D = np.array([[0.,4.],[1.,2.],[3.,8.],[6.,8.]])
diags = [D]
l=Landscape(num_landscapes=2,resolution=10).fit_transform(diags)
print(l)