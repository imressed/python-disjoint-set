# python-disjoint-set

Python based disjoint set data structure(union–find). 
Disjoint set is a data structure that keeps track of a set of elements partitioned into a number of disjoint (nonoverlapping) subsets. 

It supports two useful operations:
- **Find**: Determine which subset a particular element is in. 
          Find typically returns an item from this set that serves as its "representative";
          by comparing the result of two Find operations, one can determine whether two elements are in the same subset.
- **Union**: Join two subsets into a single subset.
