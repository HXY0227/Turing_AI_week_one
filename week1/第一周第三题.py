import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.figure(figsize=(10, 6))

plt.plot(x, y, '--', label='sin(x)')

plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

plt.xlabel('x')
plt.ylabel('y')

plt.title('三角函数')
plt.grid()
plt.legend(loc='best')
plt.show()

