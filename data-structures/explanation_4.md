User lookup is a DFS over the group tree. Check users in the current group, then recurse into child groups. Time: O(n) in number of groups/users in the subtree. Space: O(h) recursion depth.
