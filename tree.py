class Node (object) :

	def __init__(self,data):
		self.lchild = None
		self.rchild = None
		self.data = data

	def __str__(self):
		return "node : "+str(self.data) #+ " lchild : " + str(self.lchild)+ " rchild : " + str(self.rchild)

class BSTree(object):

	""" BST """

	def inorder(self,node):
		if node != None:
			self.inorder(node.lchild)
			print node.data
			self.inorder(node.rchild)

	def preorder(self,node):
		if node != None:
			print node.data
			self.preorder(node.lchild)
			self.preorder(node.rchild)

	def postorder(self,node):
		if node != None:
			self.postorder(node.lchild)
			self.postorder(node.rchild)
			print node.data

	def base_LevelOrder(self,level,node):
		if level == 0 :
			print node.data
		else :
			self.base_LevelOrder(level-1,node.lchild)
			self.base_LevelOrder(level-1,node.rchild)

	def levelorderSimple(self,node):
		# used Recursion here
		h = self.height(node)
		for level in xrange(h):
			self.base_LevelOrder(level,node)

	def levelorderQueue(self,node):
		# used Queue in LevelOrder
		a = []
		a.append(node)
		while a and len(a) > 0:
			print a[0].data
			if a[0].lchild != None :
				a.append(a[0].lchild)
			if a[0].rchild != None :
				a.append(a[0].rchild)
			a.pop(0)

	def levelorderSpiral(self,node):
		# not correct yet
		a=[]
		a.append(node)
		flag = True
		while a and len(a)>0:
			print a[0].data
			if flag :
				if a[0].lchild !=None :
					a.append(a[0].lchild)
				if a[0].rchild !=None :
					a.append(a[0].rchild)
				flag = False
			else :
				if a[0].rchild !=None :
					a.append(a[0].rchild)
				if a[0].lchild !=None :
					a.append(a[0].lchild)
				flag =True
			a.pop(0)


	def height(self,node):
		if node:
			return max(self.height(node.lchild) + 1,self.height(node.rchild) + 1)
		return 0
			


	def core_Search(self,node):
		parent_node = current_node = tree.root
		while current_node != None:
			if node.data == current_node.data :
				# print "node is present"
				break
			elif node.data > current_node.data :
				parent_node = current_node
				current_node = current_node.rchild
			else :
				parent_node = current_node
				current_node = current_node.lchild
		# else :
		# 	print "node is not present"
		return parent_node , current_node

	def insert(self,node):
		parent_node , current_node = self.core_Search(node)
		if current_node == None:
			if tree.root == None :
				tree.root  = node
			else :
				if node.data < parent_node.data :
					parent_node.lchild = node
				else :
					parent_node.rchild = node
			print str(node.data) + " is inserted"
		else :
			print "duplicate entry"

	def create_tree(self):
		n = int(raw_input("Enter no of nodes : "))
		for i in xrange(n):
			t = int(raw_input("Enter node : "))
			node = Node(t)
			tree.insert(node)

	def delete(self,node):
		parent_node , current_node = self.core_Search(node)
		if parent_node == None :
			""" 1) Parent_node is not present 
				2) Current_node is ROOT node of tree
			"""
			if current_node == None:
				print "tree is empty"
			else:
				if current_node.lchild != None and current_node.rchild != None:
					temp = self.InorderSuccessor(current_node)
					data = temp.data
					self.delete(temp)
					current_node.data = data
				else:
					if current_node.lchild != None and current_node.rchild == None:
						tree.root = current_node.lchild
					elif current_node.lchild == None and current_node.rchild != None:
						tree.root = current_node.rchild
					del(current_node)
					
		else :
			""" parent_node is present """

			if current_node == None:
				print "node is not present"
			else :
				if current_node.lchild != None and current_node.rchild != None:
					# 2 child
					temp = self.InorderSuccessor(current_node)
					data = temp.data
					self.delete(temp)
					current_node.data = data
				else:
					if current_node.lchild == current_node.rchild == None:
						# no child
						if parent_node.lchild == current_node:
							parent_node.lchild = None
						else:
							parent_node.rchild = None
					elif current_node.lchild == None and current_node.rchild != None:
						# 1 child
						if current_node == parent_node.rchild:
							parent_node.rchild = current_node.rchild
						else :
							parent_node.lchild = current_node.rchild
					elif current_node.lchild != None and current_node.rchild == None:
						# 1 child
						if current_node == parent_node.lchild:
							parent_node.lchild = current_node.lchild
						else:
							parent_node.rchild = current_node.lchild
					del(current_node)				
				
	def InorderSuccessor(self,node):
		""" InorderSuccessor is still incomplete """
		InorderSuccessor = None
		parent_node , current_node = self.core_Search(node)
		if current_node.lchild != None and current_node.rchild != None:
			""" For 2 children"""
			InorderSuccessor = current_node.rchild
			while InorderSuccessor.lchild != None:
				InorderSuccessor = InorderSuccessor.lchild
		elif current_node.lchild == current_node.rchild == None:
			""" For no children """
			pass

		else :
			""" For 1 child """
			pass

		return InorderSuccessor

	def search(self,node):
		parent_node , current_node = self.core_Search(node)
		if current_node == None :
			if parent_node == None :
				print "tree is empty"
			else :
				print "Node is not present"
		else :
			print "Node is present"

	def InorderPredecessor(self,node):
		pass

	def kthSmallestElement(self,k):
		pass

	def lca(self,node1,node2):
		""" Lowest common ancesstor """
		pass

	def BSTtoDLL(self,tree_node):
		if tree_node :
			self.BSTtoDLL(tree_node.lchild)
			self.queue.append(tree_node.data)
			self.BSTtoDLL(tree_node.rchild)

	def printAllPaths_sumFromRootToLeaf(self):
		pass



tree = BSTree()
tree.root = None
print tree

while True:
	n = int(raw_input("\n0 : create_tree \t 1 : enter node \t 2 : search \t 3 : traverse \t 4 : delete \t 5 : height\t 6:  levelorder\t 7 : BSTtoDLL \n"))
	if n==0:
		tree.create_tree()
	if n==1 :
		t = int(raw_input("provide input : "))
		node = Node(t)
		tree.insert(node)
	elif n==2 :
		t = int(raw_input("provide input : "))
		node = Node(t)
		tree.search(node)
	elif n==3 :
		tree.inorder(tree.root)
	elif n==4 :
		t = int(raw_input("provide input : "))
		node = Node(t)
		tree.delete(node)
	elif n==5 :
		print "height : " +str(tree.height(tree.root))
	elif n==6 :
		tree.levelorderSpiral(tree.root)
	elif n==7 :
		tree.queue = []
		tree.BSTtoDLL(tree.root)
		print tree.queue
		# create a DLL here via abpve Queue