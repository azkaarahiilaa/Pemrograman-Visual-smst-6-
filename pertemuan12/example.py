import tkinter as tk  # Menggunakan 'tkinter' modul

# Inisialisasi jendela utama
top = tk.Tk()

# Membuat Canvas dengan background biru, tinggi 250, dan lebar 300
C = tk.Canvas(top, bg="blue", height=250, width=300)

# Koordinat untuk arc
coord = 10, 50, 240, 210

# Membuat arc dengan koordinat yang ditentukan, mulai dari 0 derajat, dengan rentang 150 derajat, dan warna merah
arc = C.create_arc(coord, start=0, extent=150, fill="red")

# Menempatkan Canvas ke jendela utama
C.pack()

# Menjalankan main loop
top.mainloop()
