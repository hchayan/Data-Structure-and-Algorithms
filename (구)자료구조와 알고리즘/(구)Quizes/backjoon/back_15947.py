strr = """
baby sukhwan tururu turu
very cute tururu turu
in bed tururu turu
baby sukhwan
"""

list = strr.split()

num = int(input())-1

mok = num // len(list)
namugi = num % len(list)

if "ru" in list[namugi]:
	ans = list[namugi]+"ru"*mok
	if "rururururu" in ans:
		print("tu+ru*"+str((len(list[namugi])-2)//2 + mok))
	else:
		print(ans)
else:
	print(list[namugi])
	
