import tkinter as tk

# Inisialisasi root window
root = tk.Tk()

# Latihan-1: Membuat Widget Dasar
# Uncomment baris berikut untuk latihan 1
# WidgetDasarku = tk.Tk()
# WidgetDasarku.mainloop()

# Latihan-2: Membuat Canvas
# Uncomment baris berikut untuk latihan 2
# Kanvasku = tk.Canvas(root, height=500, width=500)
# Kanvasku.pack()

# Latihan-3: Membuat Frame
Frameku = tk.Frame(root, bg='blue')
Frameku.place(relwidth=0.8, relheight=0.8)

# Latihan-4a: Membuat Button di Root
# Uncomment baris berikut untuk latihan 4a
# Tombolku = tk.Button(root, text="Tes Tombol", bg='gray', fg='red')
# Tombolku.pack()

# Latihan-4b: Membuat Button di Frame
Tombolku = tk.Button(Frameku, text="Tes Tombol", bg='gray', fg='red')
Tombolku.pack()

# Latihan-5: Membuat Entry
Entryku = tk.Entry(Frameku, bg='green')
Entryku.pack()

# Menjalankan main loop
root.mainloop()
