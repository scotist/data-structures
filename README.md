[![Travis](https://travis-ci.org/scotist/data-structures.svg?branch=master)](https://travis-ci.org/scotist/data-structures.svg?branch=master)

##Data Structures

Implements various data structures of increasing complexity with python

### Simpler Structures

This repo holds sample code for some classic data structures, implemented in Python, including singly- and doubly-linked lists and stacks, heaps, queues, deques, priority queues, and graphs. Singly-linked lists are convenient for keeping a group of data nodes in order; adding and removing them is simple and efficient. They are most useful when we only need to traverse our data in one direction. Doubly-linked lists make their nodes more accessible since they can be inserted or removed at either end of the list; but navigating the list is costlier. Stacks, queues, and deques are more refined implementations.  Priority queues, heaps, and graphs illustrate more complex ways nodes of data can be related to each other.

______________

### Binary Search Tree
The binary search tree and tests include three depth-first traversal methods: in-order, pre-order, and post order; and breadth-first traversal.

The binary search tree implements a delete method, which will delete a given value from the tree, while keeping every other value and maintaining the balance of the tree.

### Hash Table
The hash table stores key-value pairs in numerical buckets where the bucket number is determined by the simple additive hashing algorithm. The hash table is initialized with an integer which determines the number of buckets and accepts only strings as keys.


### Trie
The trie is a tree data structure used to store an associative array where we care about the path to the leaf rather than the individual content of any node. Unlike the binary search tree, a node of the trie can contain any number of branches. Our implementation only accepts English words as strings. It has an insert method which accepts tokens corresponding to a single word, a contains method which returns true or false depending on whether it is present in the trie, and a traversal method which produces a generator of all the tokens in the tree. The autocomplete method returns a list of the first four arbitrarily selected tokens completing the input 'start' token, for every slice of the start token from one letter to all the letters.


### Sort Algorithms
Also included are implementations of the  insertion sort, merge sort, quick sort, and radix sort algorithms.

Insertion sort iterates over a sequence, comparing each value with the previous value and swapping them if appropriate.

Merge sort recursively divides a sequence in half and sorts the halves before merging them back togeher in order.

Quick sort divides the sequence once around an arbitary pivot and recursively sorts the values on each side of the pivot.

Radix sort compares the values from least-significant to most significant decimal, placing them in temporary buckets to create sorted order by digit.

Performance comparisons are as follows:


We tested each algorithm with a list of 990 items. We collected the average time across 10000 attempts on the best case (already sorted) and worst case (reverse sorted) lists.

Insertion Sort:
Best case average time: 0.00029
Worst case average time: 0.00032
Stability: Fully stable
In place: Yes


Merge Sort:
Best case average time: 0.0066
Worst case average time: 0.0063
Stability: Not stable with two identical items which will be sorted to far right (largest).
In place: Yes


Quick Sort:
Best case average time: 0.084
Worst case average time: 0.088
Stability: Fully stable
In place: No


Radix Sort:
Best case average time: 0.00089
Worst case average time: 0.00091
Stability: Fully stable
In place: No




Half of the modules are a joint project of Michael Sullivan and A.J. Wohlfert, and the other half of Michael Sullivan and Will Weatherford.

--------------

paren_aj.py is AJ's implementation of a function to evaluate proper parenthetical statements in a given piece of text.  If the parens are broken, a -1 will be returned, if the parens are left open, a 1 will be returned and if the parens are properly closed a 0 will be returned.


______________

parenthetics.py implements the same function as paren_aj.py, but with a different approach by Michael. There are tests for both.


______________

###Sources:

Our graph traversal functions adapt the algorithms found at:
http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/

Inspiration for the insertion sort algorithm found at:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html

https://en.wikipedia.org/wiki/Insertion_sort

For the merge sort algorithm we referenced:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

https://en.wikipedia.org/wiki/Merge_sort

For the quick sort we used referenced:
http://en.literateprograms.org/Quicksort_(Python)

The above implements quicksort using list comprehensions. We also made an implementation using plain iterations, but found that the latter method was significantly slower.

For the radix sort algorithm we adapted one found at:
https://codehost.wordpress.com/2011/07/22/radix-sort/
___________________________

