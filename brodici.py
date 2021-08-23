#Napisati program koji simulira igru potapanje brodova. Treba uneti listu od 10 redova 
#i 10 kolona, koja ce sadrzati nasumicne 0 i 1. 
#Zatim unositmo polje koje gadjamo, ako je na tom polju 1 ispisujemo pogodak i poruku 
#Pogodak, ako je 0, ispisujemo promasaj
import random
import math
def popuni(matrica):
	lista_vrsta=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
	for i in range(5):
		a=(input("Unesite vrstu (velika slova od A do H): "))
		b=int(input("Unesite kolonu(brojevi od 1 do 10):"))
		matrica[lista_vrsta.index(a)][b-1]='*'
		print('\n')

def gadjaj(matrica, i, j):
	if matrica[i][j]=='*':
		matrica[i][j]='X'
		print("Potopljeno!")
		return 0
	else:
		print("Promasaj!")
	return 1
def stampaj(matrica):
	for i in range(len(matrica)):
		print(matrica[i])

def pobeda(matrica):
	for i in range(10):
		for j in range(10):
			if matrica[i][j]=='*':
				return 1
	return 0

igrac1,igrac2=[],[]

for i in range(10):
	igrac1+=[0]
	igrac2+=[0]
for i in range(10):
	igrac1[i]=[0]*10
	igrac2[i]=[0]*10

#popuni(matrica,10,10)
i1=input("Unesite vase ime: ")
print("%s prvi igrate! \n" % i1)
i2=input("Unesite vase ime: ")
print("%s drugi igrate! \n" % i2)

print("%s popunite vasa polja, tj. napravite vase brodice." % i1)
popuni(igrac1)
print("Vasa tabla izgleda ovako: ")
stampaj(igrac1)

print("\n%s popunite vasa polja, tj. napravite vase brodice." % i2)
popuni(igrac2)
print("Vasa tabla izgleda ovako: ")
stampaj(igrac2)

print("\n")
igraci=[i1, i2]
lista_vrsta=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
i=0
k=0
while(True):
	k=k%2
	print("Igrac %s je na potezu: " % igraci[k])
	a=(input("Unesite vrstu za potapanje(slovo): "))
	b=int(input("Unesite kolonu za potapanje(broj): "))
	print("\n")
	if k==0:
		d=gadjaj(igrac2, lista_vrsta.index(a),b-1)
		if(d==0):
			k=k+1
	elif k==1:
		s=gadjaj(igrac1, lista_vrsta.index(a),b-1)
		if(s==0):
			k=k+1

	k+=1
	i+=1
	if i>=5:
		if(pobeda(igrac1)==0 or pobeda(igrac2)==0):
			print("POBEDILI STE")
			break

stampaj(igrac1)
stampaj(igrac2)