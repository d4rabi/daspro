#Nama		:
#NIM		:
#Tanggal 	:
#Deskripsi	:

from math import *

#DefSpek
#type point : < x: integer, y: integer >
#<x,y> adalah point dalam koordinat kartesian dengan x sebagai absis dan y sebagai ordinat
class point:
	def __init__(point,x,y):
		point.x = x
		point.y = y

#DefSpek
#konstruktor
#MakePoint: 2 integer --> point
#MakePoint(x,y) menghasilkan point dengan x sebagai absis dan y sebagai ordinat		
def MakePoint(x,y):
	return point(x,y)

#DefSpek
#(Selektor)
#Absis: point -> integer
#Absis (p) memberikan absis pada point p1
def Absis(p):
	return p.x

#DefSpek
#(Selektor)
#ordinat: point -> integer
#ordinat (p) memberikan ordinat di titik p
def Ordinat(p):
	return p.y

#DefSpek
#TransX: point -> point
#TransbX (p,N) menghasilkan hasil translasi P dalam sumbu x sejauh N
def TransX(p,N):
	return MakePoint(Absis(p) + N, Ordinat(p))

#DefSpek
#TransX: point -> point
#TransbX (p,N) menghasilkan hasil translasi P dalam sumbu y sejauh N
def TransY(p,N):
	return MakePoint(Absis(p), Ordinat(p) + N)

#DefSpek
#TransXY: point, 2 integer -> point
#TransXY (p,x,y) menghasilkan hasil translasi p dalam suatu x dan y
def TransXY(p,x,y):
	return MakePoint(Absis(p) + x, Ordinat(p) + y)

#DefSpek
#ReflX: point -> point
#ReflX (p) mencerminkan point terhadap sumbu x
def ReflX(p):
	return MakePoint(Absis(p), Ordinat(p) * -1)

#DefSpek
#ReflY: point -> point
#ReflY (p) mencerminkan point terhadap sumbu Y
def ReflY(p):
	return MakePoint(Absis(p) * -1, Ordinat(p))
	
#DefSpek
#IsOrigin: point -> boolean
#IsOrigin (x) benar jika x adalah titik origin (0,0)
def IsOrigin(p):
	if(Absis(p) == 0 and Ordinat(p) == 0):
		return True
	else:
		return False

#DefSpek 
#Jarak: point -> real
#Jarak (x y) menghitung jarak point X dan Y
def Jarak(p1,p2):
	return sqrt(pow(p2.x-p1.x,2) + pow(p2.y-p1.y,2))

#DefSpek
#Jarak0: point -> real
#Jarak0 (x) menghitung jarak point x terhadap titik pusat koordinat (0,0)
def Jarak0(p):
	return sqrt(pow(Absis(p),2) + pow(Ordinat(p),2))
	
#DefSpek 
#Kuadran: point -> integer [1..4]
#Kuadran (x) menghitung jarak kuadran dari point o, dengan syarat point p bukan titik origin 
#dan terletak pada sumbu x atau y
def Kuadran(p):
	if(Absis(p)>0 and Ordinat(p)>0):
		return 1
	elif(Absis(p)<0 and Ordinat(p)>0):
		return 2
	elif(Absis(p)<0 and Ordinat(p)<0):
		return 3
	elif(Absis(p)>0 and Ordinat(p)<0):
		return 4
	else:
		return 0 #tidak memiliki kuadran

