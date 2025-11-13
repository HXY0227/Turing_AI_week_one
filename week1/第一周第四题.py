import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

x = np.random.randn(100)
y = np.random.randn(100)

colors = np.random.rand(100)
sizes = np.random.rand(100) * 1000

plt.figure(figsize=(10, 8))
scatter = plt.scatter(x, y,  c=colors, s=sizes, alpha=0.3, cmap='viridis')

plt.colorbar(scatter, label='颜色值')

plt.title('汽车散点图', fontsize=16)
plt.xlabel('X坐标', fontsize=12)
plt.ylabel('Y坐标', fontsize=12)

plt.tight_layout()
plt.show()

