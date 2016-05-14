def gcd(a,b):
	if b==0:
		return a
	else :
		return gcd(b,a%b)


while  1 :
	a,b = raw_input("enter a,b ").split()
	x = gcd(int(a),int(b))
	print x
