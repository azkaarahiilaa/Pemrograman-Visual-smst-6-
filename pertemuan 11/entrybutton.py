#CREATING GUI USING TKINTER (2)
from tkinter import *
#Jalankan code untuk tiap topik bergantian. Beri tanda # # untuk topik yang #tidak dijalankan.
print('====================Exercise#1===================== ')
print('===Mencetak data dari Entry Widget dengan Button===')
print('================')
root = Tk()
root.geometry('400x200')
def CetakData():
    teks=entry1.get()
    print(teks)
    return None
entry1 = Entry (root, width = 20); entry1.pack()
Button(root, text="Cetak Data", command=CetakData).pack()
root.mainloop()
print('== =================Exercise#2==== =============')
print('===Mengambil Data dan Menampilkan Data (Part1)=====')
print('==========================')
from tkinter import *
import tkinter.messagebox
class DataInOut:

    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('300x150+0+0')
        
        frame1=Frame(self.root) 
        frame1.grid()
        
        frame2=Frame (frame1)
        frame2.grid(row=0, column=0)
        
#frame2,3,4 diletakkan pada fr
        frame3=Frame (frame1) 
        frame3.grid(row=2, column=0)
        
        frame4=Frame (frame1) 
        frame4.grid(row=2, column=1)
from tkinter import *

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title("Entry Button Example")

        frame2 = Frame(self.root)
        frame2.pack()

        FirstNum = StringVar()
        SecondNum = StringVar()

        self.lblFirstNum = Label(frame2, text='Enter First Number')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)
        self.lblSecondNum = Label(frame2, text='Enter Second Number')
        self.lblSecondNum.grid(row=1, column=0)  # Kolom diubah ke 0 untuk konsistensi
        self.txtSecondNum = Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()

print('====================Exercise#2=====================')
print('===Mengambil Data dan Menampilkan Data (Part2)=====')
print('===========================================')

from tkinter import *
import tkinter.messagebox

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('400x200+0+0')
        
        frame1 = Frame(self.root)
        frame1.grid()
        
        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)
        
        frame3 = Frame(frame1)
        frame3.grid(row=1, column=0)
        
        FirstNum = StringVar()
        SecondNum = StringVar()
        Hasil = StringVar()
        
        self.lblFirstNum = Label(frame2, text='Masukkan bilangan pertama')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)
        
        self.lblSecondNum = Label(frame2, text='Masukkan bilangan kedua')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=1, column=1)
        
        self.lblHasil = Label(frame2, text='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = Entry(frame2, textvariable=Hasil, state='readonly')
        self.txtHasil.grid(row=2, column=1)
        
        self.btnJumlahkan = Button(frame3, text='Jumlahkan', command=self.JUMLAHKAN)
        self.btnJumlahkan.grid(row=2, column=0)
        
        self.btnReset = Button(frame3, text='Reset', command=self.reset)
        self.btnReset.grid(row=2, column=1)
        
        self.btnKeluar = Button(frame3, text='Keluar', command=self.keluar)
        self.btnKeluar.grid(row=2, column=2)

    def JUMLAHKAN(self):
        try:
            pertama = float(self.txtFirstNum.get())
            kedua = float(self.txtSecondNum.get())
            hasil = pertama + kedua
            self.txtHasil.configure(state='normal')
            self.txtHasil.delete(0, END)
            self.txtHasil.insert(0, str(hasil))
            self.txtHasil.configure(state='readonly')
        except ValueError:
            tkinter.messagebox.showerror("Input Error", "Please enter valid numbers")

    def reset(self):
        self.txtFirstNum.delete(0, END)
        self.txtSecondNum.delete(0, END)
        self.txtHasil.configure(state='normal')
        self.txtHasil.delete(0, END)
        self.txtHasil.configure(state='readonly')
        self.txtFirstNum.focus()

    def keluar(self):
        self.root.destroy()

if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()
