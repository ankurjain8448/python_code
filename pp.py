# def is_power2(num):
# 	return num != 0 and ((num & (num - 1)) == 0)
# def call(a):
# 	temp = str(bin(a))
# 	tt = str(temp[2:])#parse string
# 	index = tt.rfind('1')#find last index of 1
# 	ss = list(tt)# convert string to array
# 	ss[index]='0'
# 	string = "".join(ss)#convert array to string
# 	return int(string,2)#binary to decimal conversion


# t = int(raw_input())
# for i in range(t):
# 	s = raw_input().split()
# 	a = int(s[0])
# 	b = int(s[1])
# 	if b>a:
# 		a = b
# 	ans = 0
# 	if is_power2(a):
# 		ans = a-2	
# 	else :
# 		temp= 1
# 		ans = call(a)
# 	print ans



t = int(raw_input())
s = raw_input()
lists = [int(i) for i in s.split()]
lists.sort()
count = 1
ans= []
for i in range(t):
	count-=1
	a = str(int(count) + int(lists[i]))
	ans.append(a)
print ans
s = " ".join(ans)
print s
#print "".join(ans)