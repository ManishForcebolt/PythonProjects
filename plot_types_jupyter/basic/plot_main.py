import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
# size and color:
# sizes = np.random.uniform(20, 50, len(x))
# colors = np.random.uniform(50, 100, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=20, c='b', vmin=0, vmax=100)

ax.set(xlim=(0, 9), xticks=np.arange(1, 9),
       ylim=(0, 9), yticks=np.arange(1, 9))


plt.show()
