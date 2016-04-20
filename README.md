[![Travis](https://travis-ci.org/scotist/data-structures.svg?branch=master)](https://travis-ci.org/scotist/data-structures.svg?branch=master)

Data Structures

Implements various data structures of increasing complexity with python

This repo holds sample code for some classic data structures, implemented in Python, including singly- and doubly-linked lists and stacks, heaps, queues, deques, priority queues, and graphs. Singly-linked lists are convenient for keeping a group of data nodes in order; adding and removing them is simple and efficient. They are most useful when we only need to traverse our data in one direction. Doubly-linked lists make their nodes more accessible since they can be inserted or removed at either end of the list; but navigating the list is costlier. Stacks, queues, and deques are more refined implementations.  Priority queues, heaps, and graphs illustrate more complex ways nodes of data can be related to each other.

______________


The binary search tree and tests include three depth-first traversal methods: in-order, pre-order, and post order; and breadth-first traversal.
The binary search tree implements a delete method, which will delete a given value from the tree, while keeping every other value and maintaining the balance of the tree. Also included are basic implementations of a hash table and the insertion sort algorithm.


Half of the modules are a joint project of Michael Sullivan and A.J. Wohlfert, and the other half of Michael Sullivan and Will Weatherford.

--------------

paren_aj.py is AJ's implementation of a function to evaluate proper parenthetical statements in a given piece of text.  If the parens are broken, a -1 will be returned, if the parens are left open, a 1 will be returned and if the parens are properly closed a 0 will be returned.


______________

parenthetics.py implements the same function as paren_aj.py, but with a different approach by Michael. There are tests for both.


______________

Sources:

Our graph traversal functions adapt the algorithms found at:
http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/

Inspiration for the insertion sort algorithm found at:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html

https://en.wikipedia.org/wiki/Insertion_sort

For the merge sort algorithm we referenced:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

https://en.wikipedia.org/wiki/Merge_sort
