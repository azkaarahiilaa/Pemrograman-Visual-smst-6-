import matplotlib.pyplot as plt

# Ukuran Bendera
width = 6
height = 4

# Membuat Bendera Singapura
plt.figure(figsize=(width, height))

# Warna Bendera Singapura (Merah dan Putih)
colors = ['#ed1c24', '#ffffff']

# Membuat lapangan merah pada bagian kiri bendera
plt.barh(y=1, width=1, left=0, color=colors[0], edgecolor='none')

# Membuat bagian putih di tengah bendera
plt.barh(y=1, width=1, left=1, color=colors[1], edgecolor='none')

# Membuat lapangan merah pada bagian kanan bendera
plt.barh(y=1, width=1, left=2, color=colors[0], edgecolor='none')

# Menghilangkan sumbu
plt.axis('off')

# Menampilkan Bendera Singapura
plt.show()
