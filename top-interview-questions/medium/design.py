from typing import List
import random

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''SERIALIZE AND DESERIALIZE BINARY TREE'''
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Example 1:
    # Input: root = [1,2,3,null,null,4,5]
    # Output: [1,2,3,null,null,4,5]

# Example 2:
    # Input: root = []
    # Output: []

# Constraints:
    # The number of nodes in the tree is in the range [0, 104].
    # -1000 <= Node.val <= 1000

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def pre_order(node):
            if node is None:
                serialized.append('None')
            else:
                serialized.append(str(node.val))
                pre_order(node.left)
                pre_order(node.right)
        
        serialized = []
        pre_order(root)
        return ','.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build_tree(nodes):
            if nodes[0] == 'None':
                nodes.pop(0)
                return None
            
            node_val = int(nodes.pop(0))
            node = TreeNode(node_val)
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node
        
        serialized = data.split(',')
        return build_tree(serialized)
    
'''INSERT DELETE GETRANDOM O(1)'''
# Implement the RandomizedSet class:
#     RandomizedSet() Initializes the RandomizedSet object.
#     bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
#     bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
#     int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
#      Each element must have the same probability of being returned.
#     You must implement the functions of the class such that each function works in average O(1) time complexity.

# Example 1:
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
#     RandomizedSet randomizedSet = new RandomizedSet();
#     randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
#     randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
#     randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
#     randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
#     randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
#     randomizedSet.insert(2); // 2 was already in the set, so return false.
#     randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

# Constraints:
#     -231 <= val <= 231 - 1
#     At most 2 * 105 calls will be made to insert, remove, and getRandom.
#     There will be at least one element in the data structure when getRandom is called.

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class RandomizedSet:

    def __init__(self):
        # List to store elements
        self.nums = []
        # Dict to store index of each element
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        
        # Add the element to the end of the list
        self.nums.append(val)
        # Store the index of the element in dict
        self.index_map[val] = len(self.nums)-1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        
        # Get index of element to be removed
        index = self.index_map[val]
        # Get last element in list
        last_num = self.nums[-1]

        # Swap element to be removed with last element
        self.nums[index] = last_num
        self.index_map[last_num] = index

        # Remove element from list and dict
        self.nums.pop()
        del self.index_map[val]

        return True
    

    def getRandom(self) -> int:
        return random.choice(self.nums)
