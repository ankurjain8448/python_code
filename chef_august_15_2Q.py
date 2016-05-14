def give_count(a,b):
	ans = 0
	a_index = b_index = 0
	for i in xrange(len(a)):
		pass
		if a[i]=="#":
			#do something
			





t = int(raw_input())
for i in xrange(t) :
	a = raw_input()
	b = raw_input()
	#a = [ j for j in raw_input().split()]
	#b = [ j for j in raw_input().split()]
	if a[0] == '#':
		if b[0]=="#":
			print "NO"
		else :
			a,b= b,a
			give_count(a,b)
	else :
		give_count(a,b)
