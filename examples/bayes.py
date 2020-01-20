import scipy.stats as stats
from IPython.core.pylabtools import figsize
import numpy as np
figsize(12.5, 4)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lambda1 = 0.
std1 = 1.
lambda2 = 1.
std2 = 1.5

data = stats.norm()