# Given a binary tree, find the maximum height of the binary tree.

"""

Option:
We know the current root accounts for height = 1, and then whatever the child's max height is, we add that.
So the height can be, 1 + max(height(root.left), height(root.right))

Base case: if None/NULL Node, then return 0

What is the recursive function?

"""