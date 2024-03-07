print("\033c")
#import libraries
import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#tentukan wilayah(domain) diagram catresian dan rasio lebar dan tinggi diagram
x = np.linspace(-10,10,1000)
plt.figure(figsize=(4,15))

#draw a small circle at (0,0)
# plt.plot(x, (0.05-x**2)**0.5, '-k')
# plt.plot(x, -((0.5-x**2)**0.5), '-k')

#tentukan persamaan matematika yang diinginkan
y1 = x -x -0
y2 = 0.5*x
y3 = x
y4 = 2*x
y5 = -0.5*x
y6 = -x
y7 = -2*x

plt.plot(x, y1, '-k', label='y1')
plt.plot(x, y2, '-r', label='y2')
plt.plot(x, y3, '-g', label='y3')
plt.plot(x, y4, '-b', label='y4')
plt.plot(x, y5, '-y', label='y5')
plt.plot(x, y6, '-m', label='y6')
plt.plot(x, y7, '-c', label='y7')

plt.legend(loc='upper left')
plt.grid()
plt.show()


# Mencari persamaan garis
def persamaan_garis(x1, y1, x2, y2):
    def garis(x):
        return ((y2 - y1) / (x2 - x1)) * (x - x1) + y1

    return garis

Koordinat_x1 = [2, 4]
Koordinat_y1 = [1, 2]

Koordinat_x2 = [8, 10]
Koordinat_y2 = [2, 4]

# Mencari persamaan garis
y1 = persamaan_garis(Koordinat_x1[0], Koordinat_y1[0], Koordinat_x1[1], Koordinat_y1[1])
y2 = persamaan_garis(Koordinat_x2[0], Koordinat_y2[0], Koordinat_x2[1], Koordinat_y2[1])

# Menyusun data untuk plot
x_values = [x for x in range(min(Koordinat_x1[0], Koordinat_x2[0]), max(Koordinat_x1[1], Koordinat_x2[1]) + 1)]
y_values1 = [y1(x) for x in x_values]
y_values2 = [y2(x) for x in x_values]

# Plot garis pertama
plt.plot(x_values, y_values1, '-r', label="Garis Satu")

# Plot garis kedua
plt.plot(x_values, y_values2, '-b', label="Garis Dua")

# Menampilkan plot
plt.legend()
plt.show()
