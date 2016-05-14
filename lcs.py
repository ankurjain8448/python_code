class LCSclass(object) :
	''' Printing LCS '''

	def __init__(self):
		print "******Program to Print Longest Common Subsequence******"
		a = raw_input("Enter String 1 : ")
		b = raw_input("Enter String 2 : ")
		self.lcs_matrix = self.lcs_length = None
		self.lcs = None
		''' lcs matrix will give the lcs length and then lcs matrix will give the actual lcs '''

		if len(b) > len(a):
			a,b = b,a
		self.a = a ; self.b = b


	def print_arr_matrix(self,arr):
			index = 0
			for i in arr :
				print index , i
				index+=1


	def LCS_count(self):
		a = self.a ; b = self.b
		n = len(a);m = len(b)	
		# a is larger than b and n > m and rows are less ,columns are more strategy ( m rows,n cols)
		a = "1"+a ; b = "1"+b
		# prepare array to store result.
		arr = [[0]*(n+1)]*(m+1)

		for row in xrange(1,m+1) :
			for col in xrange(1,n+1) :
				if b[row] == a[col]:
					arr[row][col] = 1 + arr[row-1][col-1]	
				else :
					arr[row][col] = max(arr[row-1][col],arr[row][col-1])

		#self.print_arr_matrix(arr)
		self.lcs_matrix = arr
		self.lcs_length = arr[m][n]
		self.lcs_last_index = (m,n)
		return  self.lcs_length

	def calculate_lcs(self):
		if not self.lcs_length :
			self.LCS_count()

		lc_main = []
		matrix = self.lcs_matrix
		i,j = self.lcs_last_index
		while True:
			if matrix[i-1][j] == matrix[i][j] :
				i-=1
			elif matrix[i][j-1] == matrix[i][j] :
				j-=1
			elif matrix[i-1][j-1]+1 ==  matrix[i][j] :
				j-=1;i-=1;lc_main.insert(0,self.a[j])				
			if i<1 or j<1 :
				break

		self.lcs = lc_main
		return self.lcs

obj = LCSclass()
print obj.calculate_lcs()
