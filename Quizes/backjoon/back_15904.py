ans = ['U','C','P','C']

inp = input()

def
t = 0
for i in inp:
	if i == ans[t]:
	  ans.remove(i)
	  if len(ans) == 0:
	    print("love")
		return
	
print("hate", ans)