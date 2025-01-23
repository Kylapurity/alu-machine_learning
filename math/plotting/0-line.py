#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Define y as the cube of values from 0 to 10
y = np.arange(0, 11) ** 3

plt.plot(np.arange(0, 11), y, color='red', linestyle='-')
plt.show()
