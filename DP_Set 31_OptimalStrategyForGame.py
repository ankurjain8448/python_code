# this code is wrong
# Ques Url : http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/

a = [20, 30, 2, 2, 2, 10]
def F(i,j):
	if i==j:
		return a[i]
	if j == i+1:
		return max(a[i],a[j])
	return max(a[i] + min(F(i+2, j), F(i+1, j-1) ),a[j] + min(F(i+1, j-1), F(i, j-2) ))

f = F(0,3)
print f
ans  = sum(a)
print ans
print ans - f