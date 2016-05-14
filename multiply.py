def multiply(a, b):
	if b==1:
		return a
	if (b%2==0):
		return multiply(a+a,b/2)
	else :
		return a+multiply(a+a,(b-1)/2 )

def mul_ineff(a, b):
  small = min(a, b)
  big = max(a, b)
  for i in xrange(small):
    big+=small
  return big

a,b  = map(int,raw_input().split())
print multiply(ans,b) 