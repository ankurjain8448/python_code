a = [i for i in xrange(10,0,-1) ]
print a

n = len(a)
for i in xrange(n-1):
#	print "i : ",i
	pass
	j = i+1
	while(j<n) :
#		print "j : ",j
		if a[i]>a[j] :
			temp = a[i]
			a[i] = a[j]
			a[j] = temp
		j+=1

print a

