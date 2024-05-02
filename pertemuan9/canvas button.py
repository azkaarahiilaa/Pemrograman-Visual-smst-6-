#CREATING GUI USING TKINTER
import tkinter as tk
#Jalankan code untuk tiap topik bergantian. Beri tanda # untuk topik yang 
# #tidak dijalankan.
root=tk.Tk()
#=========================================================
#------------------------------------------------------------------
#---------------------Latihan-1: Membuat Widget Dasar-------
#=============================================
#WidgetDasarku tk.Tk ()
# Widget Dasarku.mainloop ()
# #-------------------Latihan-2: Membuat Canvas-----
# #==========================================================
# Kanvasku = tk.Canvas (root, height = 1080, width = 1920)
# Kanvasku.pack()
#
#=================================================
#-----------Latihan-3: Membuat Canvas--------------
#==================================================
frameku=tk.Frame(root, bg='blue')
frameku.place (relwidth = 0.8, relheight = 0.8)
# # ======================================================
# #-------------------Latihan-4a: Membuat button di root-----
# #==========================================================
# Tombolku = tk.Button(root, text = "tes Tombol", bg='gray', fg = 'red')
# Tombolku.pack()

# # ======================================================
# #-------------------Latihan-4b: Membuat Canvas-----
# #==========================================================
Tombolku = tk.Button(root, text = "tes Tombol", bg='gray', fg = 'red')
Tombolku.pack()

# # ======================================================
# #-------------------Latihan-5: Membuat entry====================
Entryku = tk.Entry(frameku, bg='green')
Entryku.pack()
root.mainloop()