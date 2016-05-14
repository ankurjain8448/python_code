MAX = 100000

def SolveUsingSameArray(input_arr):
  """Print the frequency of each element in array.
  
  Args:
    input_arr: input array containing elements in range 0...N-1
  Returns:
    None, just print the frequency of each element in array
  """
  n = len(input_arr)
  # validation
  for elem in input_arr:
    assert(elem >= 0)
    assert(elem < n)
  # modify array
  for elem in input_arr:
    elem = elem % n
    input_arr[elem] += n
  # print freq and fix array
  for i in range(n):
    if input_arr[i]/n > 0:
			print "{0} appears {1} times".format(i, input_arr[i]/n)
    input_arr[i] = input_arr[i] % n
  return

def SolveUsingTable(input_arr):
  """Print the frequency of each element in array.
  
  Args:
    input_arr: input array containing elements in range 0...MAX
  Returns:
    None, just print the frequency of each element in array
  """
  n = len(input_arr)
  table = [0 for _ in range(MAX)]
  # validation
  for elem in input_arr:
    assert(elem >= 0)
    assert(elem < MAX)
  # increment count in table array
  for elem in input_arr:
    table[elem] += 1
  # print from table the elements having freq != 0
  for i in range(MAX):
    if table[i] != 0:
      print "{0} appears {1} times".format(i, table[i])
  return


def solveUsingDictionary(input_arr):
  """Print the frequency of each element in array.
  
  Args:
    input_arr: input array containing elements in range 0...MAX
  Returns:
    None, just print the frequency of each element in array
  """
  """ Using Dictionary for range 10**9 """
  n = len(input_arr)
  MAX = 10**9
  table={}
  for elem in input_arr:
    assert(elem >= 0)
    assert(elem < MAX)
    table[elem] += 1
    
  for i in range(MAX):
    if table.has_key(i):
      print "{0} appears {1} times".format(i, table[i])
  return 


input_arr = [int(elem) for elem in raw_input().split()]
SolveUsingSameArray(input_arr)