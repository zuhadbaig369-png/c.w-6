import matplotlib.pyplot as plt
import numpy as np

x = [0, 5, 10, 15, 20, 25, 30]
y1 = [0, 15, 20, 20, 30, 15, 0]
y2 = [0, 12, 15, 12, 20, 10, 0]

plt.plot(x, y1, linestyle='--', marker='D')
plt.plot(x, y2, linestyle='--', marker='D')
plt.title('Velocity-Time Graph')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Time (s)')
plt.xlim(5, 25)
plt.ylim(5, 25)
plt.legend()
plt.show()

x = np.arange(1, 11, 1)
y1 = (2*x)+1
y2 = (2*x**2)+2

plt.figure(figsize=(7, 5))
plt.plot(x, y1, 'g', linewidth=3, label='y = 2x + 1')
plt.plot(x, y2, 'r', linewidth=3, label='y = 2x^2 + 2')
plt.legend(loc='upper left')
plt.show()