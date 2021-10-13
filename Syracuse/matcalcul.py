# By judi_Co
author = "judi_Co"
#on boucle
	#si x est pére on /2
	#si x est impair on *3+1
	#faut que la somme la plus base soit pas 1
	#chech :https://vm.tiktok.com/ZM8L7jQ8Q/

import save

def checkint(n):
	if (n % 2) == 0:
		return True
	elif(n % 2) != 0:
		return False

def calcul(x):
	n = checkint(x)
	if n == True:
		x = x/2
	elif n == False:
		x = x*3+1 
	return x

def loop(i):
	ID = i
	List = []
	while True:
		i = calcul(i)
		print(i)
		List.append(i)
		if i == 1:
			Dict = {ID:[f"Iteration: {len(List)}",List]}
			save.YamlSet(Dict,"math.yml")
			break

x = 1
while True:
	print(f"on test : {x}")
	loop(x)
	x+=1