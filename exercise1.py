#!/usr/bin/env python

"""Recursion-to-Iteration Exercise 1

There are two recursive calls in find_val_or_next_smallest.

Can you create an equivalent function in which one of the
calls has been replaced by iteration?  (Hint:  Tail calls
are easier to replace.)

Can you create an equivalent function in which *both* of the
calls have been replaced by iteration?


For more information, see:
http://blog.moertel.com/tags/recursion-to-iteration%20series.html

Tom Moertel <tom@moertel.com>

"""

class BSTNode(object):
    """Binary search tree node."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '(%s, %r, %r)' % (self.val, self.left, self.right)

def find_val_or_next_smallest(bst, x, candidate=None):
    """Get the greatest value <= x in a binary search tree.

    Returns None if no such value can be found.

    """
    isDone = False

    while not isDone:
        if bst is None:
            # We've reached the bottom of the tree,
            # our current Candidate is out best option
            isDone = True
        elif bst.val == x:
            # We've found our value, no need to
            # continue searching.
            candidate, isDone = x, True
        elif bst.val > x:
            bst, candidate = bst.left, candidate
        else:  # bst.val < x
            bst, candidate = bst.right, bst.val

    return candidate

# tests

import bisect

tree0 = None
tree1 = BSTNode(5)
tree2 = BSTNode(5, BSTNode(3))
tree3 = BSTNode(5, BSTNode(3), BSTNode(9))
tree4 = BSTNode(5, BSTNode(3, BSTNode(1)), BSTNode(9))

trees = [tree0, tree1, tree2, tree3, tree4]
tree_vals = [[], [5], [3, 5], [3, 5, 9], [1, 3, 5, 9]]

if __name__ == '__main__':
    for vals, bst in zip(tree_vals, trees):
        for x in xrange(10):
            y = find_val_or_next_smallest(bst, x)
            if y is None:
                assert all(x < z for z in vals)
            else:
                assert y <= x
                if y != x:
                    i = bisect.bisect_right(vals, x)
                    assert all(x < z for z in vals[i:])
