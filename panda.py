t =  int(raw_input())
for case in xrange(t):
	n = int(raw_input())
	s = 0
	minimum = 1000000
	for i in raw_input().split():
		i = int(i)
		s+=i
		if minimum > i :
			minimum = i
	if minimum <2 :
		print -1
	else :
		print s -minimum +2