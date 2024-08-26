import matplotlib.pyplot as plt
import numpy as np


def P(list):
	newList = []
	for i in list:
		newList.append("{"+str(i)+"}")
	print(newList)

P([1,2,3])

"""

numpy.linspace(start, stop, num=50, 
endpoint=True, retstep=False, dtype=None, 
axis=0, *, device=None)

Return evenly spaced numbers over a specified interval

"""

N=10
#n = np.linspace(0,N,N)
#print(type(n))

myList = []
for i in range(10):
	myList.append(i+1)

a_n = 1/np.array(myList)

plt.plot(myList, a_n, "ro")
plt.show()