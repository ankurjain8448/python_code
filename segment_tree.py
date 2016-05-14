def sum_query():
	arr = map(int,raw_input("Enter array\n").split())
	n = len(arr)
	tree = [0]*(2*n +1)

	def get_sum(tree, ss, se, qs, qe, tree_index):
		print "tree_index : ",tree_index
		if qs <= ss or qe  >= se :
			return tree[tree_index]

		if qe < ss or qs > se :
			return 0

		mid = (ss+se)/2
		return get_sum(tree, ss, mid, qs, qe, 2*tree_index+1) + get_sum(tree, mid+1, se, qs, qe, 2*tree_index+2)

	def sum1(n,qs, qe):
		if qs < 0 or qe > n-1 or qs > qe :
			print "invalid input"
			return 0
		return get_sum(tree, 0, n-1, qs, qe, 0)

	def update_tree(tree, index, diff, ss, se, tree_index):
		if index < ss or index > se :
			return
		tree[tree_index]+=diff
		if ss!=se :
			mid = int((ss+se)/2)
			update_tree(tree, index, diff, ss,mid,2*tree_index+1)
			update_tree(tree, index, diff, mid+1,se,2*tree_index+2)


	def update(n ,val, index):
		if index < 0 or index > n-1 :
			print "invalid index"
			return
		diff = val - arr[index]
		arr[index] = val
		update_tree(tree , index, diff, 0, n-1, 0)

	def createTree(arr, tree, ss, se, tree_index):
		if ss == se :
			tree[tree_index] = arr[se]
			return arr[se]
		else :
			mid = int((ss+se)/2)
			tree[tree_index] = createTree(arr,tree,ss,mid,2*tree_index+1) + createTree(arr,tree,mid+1,se,2*tree_index+2)
			return tree[tree_index]

	createTree(arr, tree, 0, n-1, 0)
	print tree
	# update(n, 10, 2)
	print sum1(n,0, 2)
	# print tree


def min_range_query():
		
	def create_tree(ss , se, arr, tree,tree_index):
		if ss==se :
			tree[tree_index] = arr[se]
			return tree[tree_index]
		else :
			mid = int((ss+se)/2)
			tree[tree_index] = min(create_tree(ss , mid, arr, tree,2*tree_index+1),create_tree(mid+1 , se, arr, tree,2*tree_index+2))

	a = map(int,raw_input().split())
	n = len(a)
	tree = [0]*(2*n+1)
	createTree(0, n-1, arr, tree,0)