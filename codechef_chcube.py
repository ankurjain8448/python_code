t = int(raw_input())
while t:
	t-=1
	i = 0
	j = 0
	front, back, left, right, top ,bottom = map(str,raw_input().split())
	if left == front :
		 i += 1
	if left == top :
		 i += 1
	if left == bottom :
		 i += 1
	if left == back :
		 i += 1
	if i>1 :
		print "YES"
	else :
		pass
		if right == back :
			j+=1
		if right == bottom :
			j+=1
		if right == top :
			j+=1
		if right == front :
			j+=1
		if j>1 :
			print "YES"
		else :
			print "NO"