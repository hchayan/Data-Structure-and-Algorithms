import  sys

ans =""
tmp=""
flag=False

for x in sys.stdin.readline().rstrip():
	if x==" ":
		ans+=tmp+" "
		tmp=""
	elif x=="<":
		ans+=tmp
		tmp="<"
		flag=True
	elif x==">":
		ans+=tmp+">"
		tmp=""
		flag=False
	else:
		if flag == False:
			tmp = x + tmp
		else:
			tmp += x
			
ans+=tmp
print(ans)			
