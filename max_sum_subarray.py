def max_sum_subarray(arr):
	temp_ans = arr[0]
	ans = arr[0]
	for i in xrange(1,len(arr)):
		temp_ans = max(arr[i],temp_ans+arr[i])
		ans = max(ans,temp_ans)
	return ans

arr=map(int,raw_input("Enter array to fing max_subarray\n").split())
l = len(arr)
if l >0 :
	print max_sum_subarray(arr)
else :
	print "Please provide some input"