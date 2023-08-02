from typing import List
import random

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''FLATTEN 2D VECTOR'''
# Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
# Implement the Vector2D class:
#     - Vector2D(int[][] vec) initializes the object with the 2D vector vec.
#     - next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
#     - hasNext() returns true if there are still some elements in the vector, and false otherwise.

# Example 1:
# Input
#     ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
#     [[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
# Output
#     [null, 1, 2, 3, true, true, 4, false]
# Explanation
#     Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
#     vector2D.next();    // return 1
#     vector2D.next();    // return 2
#     vector2D.next();    // return 3
#     vector2D.hasNext(); // return True
#     vector2D.hasNext(); // return True
#     vector2D.next();    // return 4
#     vector2D.hasNext(); // return False

# Constraints:
#     0 <= vec.length <= 200
#     0 <= vec[i].length <= 500
#     -500 <= vec[i][j] <= 500
#     At most 105 calls will be made to next and hasNext.

# Follow up: As an added challenge, try to code it using only iterators in C++ or iterators in Java.

# Hints:
#     - How many variables do you need to keep track?
#     - Two variables is all you need. Try with x and y.
#     - Beware of empty rows. It could be the first few rows.
#     - To write correct code, think about the invariant to maintain. What is it?
#     - The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
#     - Not sure? Think about how you would implement hasNext(). Which is more complex?
#     - Common logic in two different places should be refactored into a common method.

# Your Vector2D object will be instantiated and called as such:
    # obj = Vector2D(vec)
    # param_1 = obj.next()
    # param_2 = obj.hasNext()

class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.x = 0
        self.y = 0
        self.vec = vec

    def move_to_next(self):
        while self.x < len(self.vec) and self.y >= len(self.vec[self.x]):
            self.x += 1
            self.y = 0

    def next(self) -> int:
        self.move_to_next()
        if self.x < len(self.vec):
            val = self.vec[self.x][self.y]
            self.y += 1
            return val
        return None

    def hasNext(self) -> bool:
        self.move_to_next()
        return self.x < len(self.vec)
    
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

'''DESIGN TIC-TAC-TOE'''
# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
    # - A move is guaranteed to be valid and is placed on an empty block.
    # - Once a winning condition is reached, no more moves are allowed.
    # - A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Implement the TicTacToe class:
#     - TicTacToe(int n) Initializes the object the size of the board n.
#     - int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
#         0 if there is no winner after the move,
#         1 if player 1 is the winner after the move, or
#         2 if player 2 is the winner after the move.

# Example 1:
# Input
#     ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
#     [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
#     Output
#     [null, 0, 0, 0, 0, 0, 0, 1]

# Explanation
#     TicTacToe ticTacToe = new TicTacToe(3);
#     Assume that player 1 is "X" and player 2 is "O" in the board.
#     ticTacToe.move(0, 0, 1); // return 0 (no one wins)
#     |X| | |
#     | | | |    // Player 1 makes a move at (0, 0).
#     | | | |

#     ticTacToe.move(0, 2, 2); // return 0 (no one wins)
#     |X| |O|
#     | | | |    // Player 2 makes a move at (0, 2).
#     | | | |

#     ticTacToe.move(2, 2, 1); // return 0 (no one wins)
#     |X| |O|
#     | | | |    // Player 1 makes a move at (2, 2).
#     | | |X|

#     ticTacToe.move(1, 1, 2); // return 0 (no one wins)
#     |X| |O|
#     | |O| |    // Player 2 makes a move at (1, 1).
#     | | |X|

#     ticTacToe.move(2, 0, 1); // return 0 (no one wins)
#     |X| |O|
#     | |O| |    // Player 1 makes a move at (2, 0).
#     |X| |X|

#     ticTacToe.move(1, 0, 2); // return 0 (no one wins)
#     |X| |O|
#     |O|O| |    // Player 2 makes a move at (1, 0).
#     |X| |X|

#     ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
#     |X| |O|
#     |O|O| |    // Player 1 makes a move at (2, 1).
#     |X|X|X|

# Constraints:
#     2 <= n <= 100
#     player is 1 or 2.
#     0 <= row, col < n
#     (row, col) are unique for each different call to move.
#     At most n2 calls will be made to move.
 
# Follow-up: Could you do better than O(n2) per move() operation?

# Hints:
#     - Could you trade extra space such that move() operation can be done in O(1)?
#     - You need two arrays: int rows[n], int cols[n], plus two variables: diagonal, anti_diagonal.

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        mark = 1 if player == 1 else -1

        # Update row and column count for current player
        self.rows[row] += mark
        self.cols[col] += mark

        # Check if current move is in main diagonal
        if row == col:
            self.diagonal += mark

        # Check if current move is in anti-diagonal
        if row + col == self.n - 1:
            self.anti_diagonal += mark

        # Check if current player wins
        if (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.diagonal) == self.n
            or abs(self.anti_diagonal) == self.n
        ):
            return player

        return 0