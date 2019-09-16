#Nama		:
#NIM		:
#Tanggal 	:
#Deskripsi	:

#DefSpek
#pangkat2 : integer -> integer
#Pangkat2(x) menghitung x^2
def pangkat2(x) :
	return(x*x)

#DefSpek
#Lling : integer -> integer
#Lling(x) menghitung luas lingkaran dengan fungsi pangkat
def Lling(x) :
	return((22 / 7) * pangkat2(x))

#DefSpek
#persegi : integer -> integer
#persegi(x) menghitung luas persegi
def persegi(x) :
	return(x*x)

#DefSpek
#lpkubus(x) menghitung luas permukaan kubus dengan memanggil fungsi persegi
def lpkubus(r) :
	return(persegi(r)*6)

#DefSpek
#max : 2 integer -> integer
#max(x,y) mencari nilai maksimum dari dua bilangan 
def max2(a, b) :
	if (a > b) :
		return(a)
	else:
		return(b)