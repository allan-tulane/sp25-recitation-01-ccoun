"""
CMPS 2200  Recitation 1
Name (Team Member 1): Charlie Coun
Name (Team Member 2): Vincent Camacho
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	""" The worst case input value for linear_search is a list where the key is not in the list. This will have a runtime of O(N), as it will 			iterate through the entire list. The best case input value for linear_search is a list where the key is first value the list. This 					will have a runtime of O(1)"""
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	""" The worst case input value for binary_search is a list where the key is not in the list, as it will run Log(base 2)(N) times. The 					best case run time complexity for binary_search is O(1) as it will run once if the key is at the mid position which is equal to (left 			+ right)//2 in the list."""
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO
	if left > right:
		return -1

	mid = (left + right) // 2

	if mylist[mid] == key:
		return mid

	elif mylist[mid] > key:
		return _binary_search(mylist, key, left, mid - 1)

	else: 
		return _binary_search(mylist, key, mid + 1, right)
	###




def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	start = time.time()
	search_fn(mylist, key)
	end = time.time()
	return (end - start) * 1000
	

	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	results = []
	for size in sizes:
		n = int(size)
		mylist = list(range(n))

		linear_time = time_search(linear_search, mylist, -1)
		binary_time = time_search(binary_search, mylist, -1)

		results.append((n, linear_time, binary_time))

	return results

	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

print_results(compare_search())
"""
|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.002 |    0.003 |
|      100 |    0.003 |    0.001 |
|     1000 |    0.037 |    0.002 |
|    10000 |    0.456 |    0.004 |
|   100000 |    4.571 |    0.005 |
|  1000000 |   45.757 |    0.014 |
| 10000000 |  496.446 |    0.016 |
"""
"""
Answer for 9: Our empirical results match the runtimes of O(N) for the linear search and O(Log(N)) for the binary search. As seen in the runtimes, when n increases by 10, the runtimes for the linear search increase at a much more rapid pace, getting to over a minute long for an input size of 10 million. However for the binary search, the runtimes are much slower, getting to around 0.5 seconds for an input size of 10 million. This mimics the behavior of the linear vs logarithmic graphs with respect to runtime.
"""
"""
Answer for 10: The worst case complexity of searching a list of n elements k times using linear search is O(N*K), where K is the number of times the key is found. The worse case complexity of searching a list of n elements k times using binary search is O(K*Log(N)), where K is the number of times the key is found. It is more efficient to first sort and then use binary search instead of simply using linear search without sorting when K is very large. For smaller searches, linear search is more efficient. 
"""