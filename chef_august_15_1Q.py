import math

def is_perfect_power(n):
	x = int(math.log(n)/math.log(2))
	if 2**x == n :
		return True
	return False

def count(a,b):
	if is_perfect_power(a):
		return abs(int(math.log(b)/math.log(2)) - int(math.log(a)/math.log(2)))
	else :
		if a%2==0 :
			return count(a/2,b) + 1
		else :
			return count((a-1)/2,b) + 1

t = int(raw_input())
for i in xrange(t) :
	a = [int(j) for j in raw_input().split()]
	y = a[1]
	x = a[0]
	print count(x,y)

