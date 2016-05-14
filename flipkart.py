arr = ['i=j','k>n','j>k','l>k']
equal_pair = {}
greater_pair={}
greater_pair_count = 0

for i in arr :
	a = i[0]
	sign = i[1]
	b = i[2]
	if sign == '=':
		equal_pair[a] = b
	elif sign == '>':
		greater_pair[a]=b
		greater_pair_count+=1
	else :
		greater_pair[b]=a
		greater_pair_count+=1

ans = []
print "greater_pair : " , greater_pair
print "equal_pair : " ,equal_pair
temp = None
while greater_pair_count:
	if not temp :
		# print "temp is none"
		for key , value in greater_pair.items() :
			del greater_pair[key]
			if not len(ans):
				ans.append(key)
				ans.append('>')
				ans.append(value)
				temp = value
			else :
				try:
					i = ans.index(value)
					ans.insert(i,'>')
					ans.insert(i,key)
				except ValueError:
					ans.append(key)
					ans.append('>')
					ans.append(value)
					temp = value
			greater_pair_count-=1
			break
	else :
		value = greater_pair.get(temp,None)
		if value :
			del greater_pair[temp]
			i = ans.index(temp)
			ans[i:] = '>'
			ans[i+1:] = value
			temp = value
			greater_pair_count-=1
		else :
			temp = None

for key,value in equal_pair.items():
	if key in ans :
		i = ans.index(key)
		ans.insert(i,value)
		ans.insert(i+1,'=')		
	elif value in ans :
		i = ans.index(value)
		ans.insert(i,key)
		ans.insert(i+1,'=')
# if loop_count > greater_pair_count :
# 	print "something is wrong"
print ans