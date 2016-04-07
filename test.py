from disjoint_set import DisjointSet


if __name__=='__main__':
	test_set = DisjointSet([1,2,3,3,3,4,5,6,7,7,7,7])
	
	print test_set.get()
	
	print test_set.union(2,3)
	print test_set.union(6,7)
	
	print test_set.union(7,10)
	
	print test_set.union(2,6)