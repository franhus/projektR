import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y_unutarnji = np.sin(x)        # Donji rub
y_vanjski = np.sin(x) + 2.0    # Vanjski rub (2 jedinice iznad)

# Bojimo prostor između unutarnjeg i vanjskog ruba
plt.fill_between(x, y_unutarnji, y_vanjski, color='gray', alpha=1, label='Asfalt staze')

# Nacrtajmo i same rubove da ljepše izgleda
plt.plot(x, y_unutarnji, 'r-', label='Unutarnji rub')
plt.plot(x, y_vanjski, 'b-', label='Vanjski rub')

plt.legend()
plt.show()