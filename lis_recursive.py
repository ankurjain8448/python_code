def LIS(a):
	n = len(a)
	lis =[1]*n
	for i in xrange(n):
		for j in xrange(n):
			if a[i]<a[j] & lis[i]<lis[j]+1:
				lis[i] = lis[j]+1

	print max(lis) + 1
	print "lIS"
	print lis

a = [10,22,9,33,20,50,41,60,80]
LIS(a)


def LIS2(a):
	print a
	n = len(a)
	lis = [1]*n
	j = 0
	for i in xrange(1,n):
		j = i-1
		while j>=0:
			if a[i]>a[j]:
				break
			j-=1
		print i,j
		if j!=-1:
			lis[i] = 1+ max(lis[:j+1])
	print lis
	print lis[n-1]

a = [10,22,9,33,20,50,41,60,80]
# LIS2(a)