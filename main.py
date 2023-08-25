import matplotlib.pyplot as plt
import random
x = []
y = []
for i in range(10):
    x.append(random.randint(1,20))
    y.append(random.randint(1,20))

plt.scatter(x, y, color='red')
plt.show()