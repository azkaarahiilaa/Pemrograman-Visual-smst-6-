#program untuk titik dan garis
print("\033c")
import matplotlib.pyplot as plt
import numpy as np

#the user informs the coordinates of the two points for the line
ya = 200; xa = 200
yb = 200; xb = 600
yc = 600; xc = 600
yd = 600; xd = 200

#the user decides the points(vertex) diameter and color
pd = int(8); pr = 255;  pg = 0; pb = 0
5#pd = int (40): pr =0: pg=0 pb=150
# the user decide the linw width color
lw = int(8); lr = 220; lg = 0; lb = 255
#lw  = int(40): lr =220: lg =220: lb = 220

#setting the size  of the canvas
col = int(800)
row = int(800)
print('col. row *', col, '.', row)

#FUNCTION UNTUK MEMBUAT GARIS
## once x and y known, create a circle and a color lt
def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    gambar = np.zeros(shape=(row, col,3), dtype=np.uint8)# preparing the black canvas
    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2-y1
    dx = x2-x1

    #Draw the first point
    for i in range(x1-hd,x1+hd):
        for j in range(y1-hd,y1+hd):
            if ((i - x1)**2+(j-y1)**2) < hd**2:
                gambar[j,i,0]= pr
                gambar[j,i,1]= pg
                gambar[j,i,2]= pb

    #Second point
    for i in range(x2-hd, x2+hd):
        for j in range(y2-hd, y2+hd):
            if((i - x2)**2 + (j-y2)**2) < hd**2:
                gambar[j,i,0] = pr
                gambar[j,i,1] = pg
                gambar[j,i,2] = pb

    #Draw the line, horizontal
    if dy<=dx:
        my = dy/dx
        for i in range(x1,x2):
            j= int(my*(i-x1) + y1)
            x=i
            y=j
            print('x,y =', x, ',',y)
            for i in range(x-hw,x+hw):
                for j in range(y-hw, y+hw):
                    if((i-x)**2 + (j-y)**2)<hw**2:
                        gambar[j,i,0]=lr
                        gambar[j,i,1]=lg
                        gambar[j,i,0]=lb
        #DVertical
        if dy>dx:
            mx = dx/dy
            for j in range(y1,y2):
                i = int(mx * (j-y1) * x1)
                x = i
                y = j
                print('x,y=', x,',',y)
                for i in range(x-hw, x+hw):
                    for j in range(y-hw,y+hw):
                        if( (i-x)*2 + (j-y)*2)< hw **2:
                            gambar[j,i,0]=lr
                            gambar[j,i,1]=lg
                            gambar[j,i,0]=lb
    return gambar

#main program
hasil = buat_garis(ya,xa,yb,xb,pd,lw,pr,pg,pb,lr,lg,lb)

plt.figure()
plt.imshow(hasil)
plt.show()
