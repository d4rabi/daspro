#Nama		:
#NIM		:
#Tanggal 	:
#Deskripsi	:

#DefSpek
#jenis bilangan : integer -> integer
#jenis bilangan (x) mencari jenis bilangan positif, negatif, atau no
def jenisbilangan(x) :
	if (x == 0) :
		return("a = 0")
	elif (x >  0) :
		return("positif")
	else :
		return("negatif")

#DefSpek
#max9 : integer -> integer
#mencari bilangan terbesar dari 9 bilangan integer
def max4(a,b,c,d) :
	return(max (max3_1(a,b,c), d))

def max9(a,b,c,d,e,f,g,h,i) :
	return(max(max(max(max(max(max(max(max(a,b),c),d),e),f),g),h),i))

def max9_1(a,b,c,d,e,f,g,h,i) :
	return(max3_1(max3_1(a,b,c),max3_1(d,e,f),max3_1(g,h,i)))

#DefSpek
#IsValid : integer -> boolean
#IsValid (x) benar jika x bernilai lebih dari 0 dan kurang dari 100
def IsValid(x) :
	if ((x > 0) and (x > 100)) :
		return("Valid")
	else :
		return("Invalid")

#DefSpek
#cumlaude : real-> string
#3.5 cumlaude
#2.76 - 3.5
#< 2.76
def cumlaude(x) :
	if ((x >= 3.5) and (x <= 4)) :
		return("Cumlaude")
	elif ((x >= 2.76) and (x < 3.5)) :
		return("Sangat memuaskan")
	else :
		return("maaf anda belum beruntung")