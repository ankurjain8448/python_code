# craftsvilla LuckyNumber Question
import math
t = int(raw_input())
while t:
	t-=1
	n = int(raw_input())
	if n < 3 :
		print 0
	else :
		power = math.log(n)/math.log(2)
		temp = 2
		ans = 0
		for each_pow in xrange(1,power+1):
			val = 2**each_pow
			temp = 0
			k = 1
			for i in xrange(each_pow):
				k = k*2
				temp = temp + val + k


			pass
		print ans



# t = int(raw_input())
# d= {}
# mod = 1000000007
# def solve(arr,n,total):
# 	l = len(arr) - 1
# 	arr[1] = '0'
# 	arr[l] = '1'
# 	flag = True
# 	while l > 0:
# 		s = ''.join(arr)
# 		bin = int(s,2)
# 		if bin <= n :
# 			bin = bin%mod
# 			total += bin
# 			total = total%mod
# 			d[bin] = total
# 		else :
# 			flag = False
# 			break
# 		l-=1
# 		arr[l] , arr[l+1] = arr[l+1] , arr[l] 
# 	return flag , total

# while t:
# 	t-=1
# 	n = int(raw_input())
# 	arr= ['1','1']
# 	flag = True
# 	total = 0
# 	if n < 2 :
# 		flag = False
# 	else :
# 		if n in d :
# 			total = d[n]
# 			flag = False
# 		while flag:
# 			flag , total = solve(arr,n,total)
# 			total =  total% mod
# 			arr.append('0')
# 	d[n] = total
# 	print total

# t = int(raw_input())
# d= {}
# d[0] = 0
# d[1] = 0
# d[2] = 0
# mod = 1000000007
# maximum = 2
# def solve(arr,n,total):
# 	l = len(arr) - 1
# 	arr[1] = '0'
# 	arr[l] = '1'
# 	flag = True
# 	while l > 0:
# 		s = ''.join(arr)
# 		bin = int(s,2)
# 		if bin <= n :
# 			bin = bin%mod
# 			total += bin
# 			total = total%mod
# 			# d[bin] = total
# 		else :
# 			flag = False
# 			break
# 		l-=1
# 		arr[l] , arr[l+1] = arr[l+1] , arr[l] 
# 	return flag , total
# import math
# while t:
# 	t-=1
# 	n = int(raw_input())
# 	arr= ['1','1']
# 	flag = True
# 	total = 0
# 	if n < 2 :
# 		flag = False
# 	else :
# 		if n > maximum :
# 			x = 2**int(math.log(maximum)/math.log(2))
# 			total = d[x]
# 			for i in xrange(2,len(bin(x)[2:])):
# 				arr.append('0')
# 			while flag:
# 				flag , total = solve(arr,n,total)
# 				total =  total% mod
# 				arr.append('0')
# 		else :
# 			if n in d :
# 				total = d[n]
# 				flag = False
# 			else :		
# 				x = 2**int(math.log(n)/math.log(2))
# 				if x in d:						
# 					total = d[x]
# 					for i in xrange(2,len(bin(x)[2:])):
# 						arr.append('0')
# 				while flag:
# 					flag , total = solve(arr,n,total)
# 					total =  total% mod
# 					arr.append('0')
# 	d[n] = total%mod
# 	maximum = max(maximum,n)
# 	print total