import matplotlib.pyplot as plt

# Ukuran Bendera
width = 6
height = 4

# Membuat Bendera Indonesia
plt.figure(figsize=(width, height))

# Warna Bendera Indonesia (Merah dan Putih)
colors = ['#ed1c24', '#ffffff']

# Membuat garis merah pada bagian kiri bendera
plt.barh(y=1, width=0.5, left=0, color=colors[0], edgecolor='none')

# Membuat bagian putih di tengah bendera
plt.barh(y=1, width=0.5, left=0.5, color=colors[1], edgecolor='none')

# Menghilangkan sumbu
plt.axis('off')

# Menampilkan Bendera Indonesia
plt.show()
