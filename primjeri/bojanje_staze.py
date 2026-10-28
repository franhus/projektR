import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y_unutarnji = np.sin(x)
y_vanjski = np.sin(x) + 2.0

plt.fill_between(x, y_unutarnji, y_vanjski, color='gray')

plt.plot(x, y_unutarnji, 'b-')
plt.plot(x, y_vanjski, 'b-')

plt.show()