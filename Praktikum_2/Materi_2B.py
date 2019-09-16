#Nama		:
#NIM		:
#Tanggal 	:
#Deskripsi	:

#DefSpek
#max3_1 : 3 integer -> integer 
#max3_1 (x y z) mencari nilai max dari 3 bilangan menggunakan fungsi max2
def max3_1(x,y,z) :
	return(max2 (max2(x,y), z))

#DefSpek
#max3_2 : 3 integer -> integer
#max3_2 x y z menggunakan nilai max dari 3 bilangan dengan menggunakan kondisi
def max3_2(a,b,c) :
	if (max2(a,b) < c) :
		return(c)
	else :
		return(max2(a,b))
		
# DefSpek
# FungsiKondisi1 : integer -> string
# FungsiKondisi1 (a b) mengetahui bilangan mana yang lebih besar
def FungsiKondisi1(a,b) :
	if (a == b) :
		return("a sama dengan b")
	elif (a > b) :
		return("a lebih besar b")
	else :
		return("a kurang dari b")

# DefSpek 
# FungsiKondisi2 : integer -> string
# FungsiKondisi2 (a b) mengetahui kedua bilangan sama atau tidak
def FungsiKondisi2(a,b) :
	if (a == b) :
		return("a sama dengan b")
	else :
		return("a tidak sama dengan b")
