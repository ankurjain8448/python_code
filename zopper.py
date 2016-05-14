a,b = raw_input().split()
a = int(a)
b = int(b)
time= 0
n = int(raw_input())
data = [ int(i) for i in raw_input().split() ]
data.sort()
if b%a==0 and data[0] == 1:
	time=1
elif b%a==0 and data[0] == 1:
	print -1
else :	
	index = 0
	while b > 0 and index < n:
		i = data[index]
		if b%i==0:
			b = b/i
			time+=1
		index+=1
print time

		