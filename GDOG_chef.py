from fractions import gcd
n = int(raw_input())
a = [ int(i) for i in raw_input().split() ]
fx = 1
gx = 1
mod = 1000000007
flag = True

for i in a:
	fx = (fx*i)%mod
	
for i in xrange(0,len(a)-1,2):
	temp = gcd(a[i],a[i+1]
	if flag:
		flag = False
		gx = temp
	else :
		gx = gcd(gx,temp)
		
	if gx == 1:
		break
print (fx**gx)%mod

# n = int(raw_input())
# n = 2**n - 1
# d = {}
# for i in xrange(n):
# 	pass
# 	a,b = raw_input().split()
# 	if a not in d :
# 		d[a] = 1
# 	d[b] = -1

# for i in d :
# 	if d[i]==1:
# 		print i
# 		break







# n = int(raw_input())
# for i in xrange(n):
# 	ans = 2
# 	num = int(raw_input())
# 	for i in xrange(2,num/2+1):
# 		if n%i==0:
# 			ans++
# 			if ans == 4:
# 				print "NO"
# 				break
# 	else :
# 		print "YES"

# a,b = raw_input().split()
# a = int(a)
# b = int(b)
# ans = 0
# string = raw_input()
# for i in string :
# 	if i=='1':
# 		ans+=a
# 		ans = ans%b
# 	a = (a**2)%b
# print ans

# t = int(raw_input())
# mod = 1000000007
# for i in xrange(t):
# 	n = int(raw_input()) -1
# 	ans = (n*(n+1))/2
# 	ans+=1
# 	ans  = ans % mod
# 	print ans

# t = int(raw_input())
# for i in xrange(t):
# 	n , k = raw_input().split()
# 	n = int(n)
# 	k = int(k)
# 	ans = 0
# 	for j in xrange(1,k+1):
# 		if n%j > ans :
# 			ans = n%j

# 	print ans

# s = raw_input()
# s = s[::-1]
# ans = ""
# count = 0
# for i in s:
# 	j = int(i)
# 	if j%2==0:
# 		count+=1
# 	ans = ans+str(count)+" "
# ans = ans[::-1]
# print ans[1:]