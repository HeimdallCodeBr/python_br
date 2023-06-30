import numpy as np
import os 

os.system('clear')


a = ([10, 4, 7], [5, 2, 7], [0, 1, 3])
b = ([10, 4, 7], [5, 0, 7], [0, 7, 4])
a1 = np.array(a)
b1 = np.array(b)

c = np.diag(a1)
print(a1)
print(c)
