# kepala mickey mouse

print("\033c")
import matplotlib.pyplot as plt
import numpy as np

# Tentukan wilayah (domain) diagram cartesian dan rasio dan lebar dan tinggi diagram
x = np.linspace(-12, 12, 10000)
plt.figure(figsize=(12, 12))

# Tentukan persamaan matematika yang diinginkan
y = x - x - 0
y1 = 5 + (5 - x**2)**0.5
y2 = 5 - (5 - x**2)**0.5

y3 = 7 + (2 - (x - 2.2)**2)**0.5
y4 = 7 - (2 - (x - 2.2)**2)**0.5

y7 = 7 + (2 - (x + 2.2)**2)**0.5
y8 = 7 - (2 - (x + 2.2)**2)**0.5

plt.plot(x, y, '-r')
plt.plot(x, y1, '-k', label='y1, y2')
plt.plot(x, y2, '-k')
plt.plot(x, y3, '-k', label='y3, y4')
plt.plot(x, y4, '-k')
plt.plot(x, y7, '-k', label='y7, y8')
plt.plot(x, y8, '-k')

# Isi area di antara kurva
plt.fill_between(x, y1, y2, color='black')
plt.fill_between(x, y3, y4, color='black')
plt.fill_between(x, y7, y8, color='black')

plt.axis('equal')
plt.legend(loc='upper center')
plt.grid()
plt.show()
