from pyrivet import rivet
import numpy as np

# The RIVET distribution comes with some test data files
import os

rivet_location = '/Users/sinanunver/Documents/GitHub/persistence/pyrivet' #Might be in a different location for you
print(os.listdir(rivet_location + '/aspirin-ZINC0000000000053.sdf.txt'))