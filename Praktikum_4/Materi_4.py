#Nama		:
#NIM		:
#Tanggal 	:
#Deskripsi	:

from math import *

#DefSpek
#Jumlah : 2 integer -> integer
#Jumlah(a,b) menghasilkan penjumlahan a dan b menggunakan prinsip rekursif
def Jumlah(a,b):
	if(b == 0):
		return a
	else:
		return 1 + Jumlah(a, b-1)

#DefSpek
#Kali : 2 integer -> integer
#Kali(a,b) menghasilkan perkalian a dan b menggunakan prinsip rekursif
def Kali(a,b):
	if(b == 1):
		return a
	else:
		return a + Kali(a, b-1)

#DefSpek
#Pangkat : 2 integer -> integer
#Pangkat(a,b) menghasilkan a pangkat b menggunakan prinsip rekursif
def Pangkat(a,b):
	if(b == 0):
		return 1
	else:
		return a * Pangkat(a, b-1)

#DefSpek
#Fibonacci : integer -> integer
#Fibonacci(n) menghasilkan bilangan fibonacci ke-n
def Fibonacci(n):
	if(n == 0):
		return 0
	elif(n == 1):
		return 1
	else:
		return Fibonacci(n-2) + Fibonacci(n-1)

#DefSpek
#IsGanjil : integer > 0 -> boolean
#IsGanjil(n) menghasilkan True bila n ganjil
def IsGanjil(n):
	if(n == 1):
		return True
	elif(n == 0):
		return False
	else:
		return IsGanjil(n-2)
		
#DefSpek
#IsGenap : integer > 0 -> boolean
#IsGenap(n) menghasilkan True bila n genap
def IsGenap(n):
	if(n == 0):
		return True
	elif(n == 1):
		return False
	else:
		return IsGenap(n-2)
		
#DefSpek
#Fak : integer > 0 -> integer > 0
#Fak(n) menghasilkan faktorial dari n
def Fak(n):
	if(n == 0):
		return 1
	else:
		return Fak(n-1)*n
		
#DefSpek
#FakIteratif : integer > 0 -> integer
#FakIteratif(n) menghasilkan faktorial dari n
#FakIter : 3 integer > 0 -> integer
#FakIter(n,count,hasil) mengahsilkan hasil faktorial dengan iteratif
def FakIter(n,count,hasil):
	if(n == count):
		return hasil * count
	else:
		return FakIter(n, count+1, hasil*count)

def FakIteratif(n):
	return FakIter(n,1,1)
	
def tama(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	elif (n == 2):
		return 2
	else:
		return tama(n-3) + tama(n-2) + tama(n-1)