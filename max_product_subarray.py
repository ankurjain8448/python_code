def max_product_subarray(a):
	"""Its an O(n) solution with O(1) space complexity"""
	ans = 1
	positive_ans = 1
	negative_ans= 1
	is_one = False
	for i in xrange(len(a)):
		if a[i]==1:
			is_one = True
		if a[i]>0:
			positive_ans *=a[i]
			negative_ans = negative_ans*a[i]
		elif a[i] == 0:
			positive_ans = 1
			negative_ans = 1
		else :
			temp = positive_ans
			positive_ans = max(negative_ans*a[i],1)
			negative_ans = temp*a[i]

		if positive_ans > ans:
			ans = positive_ans
		if ans == 1 :
			if not is_one :
				ans = 0
	return ans
	
a = map(int,raw_input("enter array \n").split())
print max_product_subarray(a)
