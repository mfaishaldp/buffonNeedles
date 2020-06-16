import turtle
from random import *

myPen = turtle.Turtle()
myPen.ht()
myPen.speed(0)
myPen.color('black')

l = 40                 # panjang jarum
d = 50                 # panjang / jarak antar garis
J = 100                # Jumlah jarum yang di jatuhkan
hits = 0               # Jumlah jarum yang mengenai garis (masih inisiasi di nolkan)
phieksak = 3.141592654 # nilai phi eksak



# garis untuk lintasan dengan jarak antar garis d
for i in range(-95, 125, d):
    myPen.pu()
    myPen.setpos(-125, i)
    myPen.pd()
    myPen.fd(280)  # panjang garis

# Jarum
myPen.color('blue')
for j in range(J):
    myPen.pu()
    myPen.goto(randrange(-125, 125), randrange(-95, 105))
    y1 = myPen.ycor()  
    myPen.seth(360*random())
    myPen.pd()
    myPen.fd(l)    # jarum dengan panjang = l
    y2 = myPen.ycor()  

    # menghitung banyak jarum yang mengenai garis
    if y1//20 != y2//20:    # cek apakah mengenai garis (hits)
        hits += 1           # jika kena garis hits akan +1


phiestimasi = ((2*(l/10)*J) / (hits * (d/10))) # dibagi 10 karena dari mm ke cm
eror = phieksak - phiestimasi
print("Jumlah jarum yang terkena garis : " + str(hits))
print("PHI ESTIMASI= "+ str(phiestimasi))
print("PHI EKSAK = " + str(phieksak))
print("ERROR = " + str(eror))