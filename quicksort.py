import random
a = map(int,xrange(10,0,-1))
print a
n = len(a) - 1
def quickSort(start,end):		
	if start >= end:
		return
	x = pivot = start
	y = end
	start+=1
	while start<end :
		while start<end and a[pivot] > a[start]:
			start+=1
		while start<end and a[end] > a[pivot]:
			end-=1
		a[start],a[end] = a[end],a[start]

		
	if a[pivot] <a[end] :
		end-=1

	a[pivot],a[end] = a[end],a[pivot]
	quickSort(x,end-1)	
	quickSort(end+1,y)
				

quickSort(0,n)
print a


# def sortA(array):
#     less = []
#     equal = []
#     greater = []

#     if len(array) > 1:
#         pivot = array[0]
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             if x == pivot:
#                 equal.append(x)
#             if x > pivot:
#                 greater.append(x)
#         # Don't forget to return something!
#         return sortA(less)+equal+sortA(greater)  # Just use the + operator to join lists
#     # Note that you want equal ^^^^^ not pivot
#     else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
#         return array

# a = [12,4,5,6,7,3,1,15]
# print a
# print sortA(a)
