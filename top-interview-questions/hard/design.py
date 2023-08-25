from typing import List, NestedInteger
import heapq

'''LRU CACHE'''
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:
# - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# - int get(int key) Return the value of the key if the key exists, otherwise return -1.
# - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:
#     Input
#         ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#         [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#     Output
#         [null, null, null, 1, null, -1, null, -1, 3, 4]
#     Explanation
#         LRUCache lRUCache = new LRUCache(2);
#         lRUCache.put(1, 1); // cache is {1=1}
#         lRUCache.put(2, 2); // cache is {1=1, 2=2}
#         lRUCache.get(1);    // return 1
#         lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
#         lRUCache.get(2);    // returns -1 (not found)
#         lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#         lRUCache.get(1);    // return -1 (not found)
#         lRUCache.get(3);    // return 3
#         lRUCache.get(4);    // return 4

# Constraints:
#     1 <= capacity <= 3000
#     0 <= key <= 104
#     0 <= value <= 105
#     At most 2 * 105 calls will be made to get and put.

# Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.order = []  # List to maintain the order of keys based on their usage

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the key to the end of the order list to indicate recent usage
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key exists, update the value and move the key to the end of the order list
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is full, evict the least recently used key (first key in the order list)
                lru_key = self.order[0]
                del self.cache[lru_key]
                self.order.pop(0)
            # Add the new key-value pair to the cache and the end of the order list
            self.cache[key] = value
            self.order.append(key)

'''IMPLEMENT TRIE (PREFIX TREE)'''
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Example 1:
#     Input
#         ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#         [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
#     Output
#         [null, null, true, false, true, null, true]
#     Explanation
#         Trie trie = new Trie();
#         trie.insert("apple");
#         trie.search("apple");   // return True
#         trie.search("app");     // return False
#         trie.startsWith("app"); // return True
#         trie.insert("app");
#         trie.search("app");     // return True

# Constraints:
#     1 <= word.length, prefix.length <= 2000
#     word and prefix consist only of lowercase English letters.
#     At most 3 * 104 calls in total will be made to insert, search, and startsWith.

# Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        
        return True

'''FLATTEN NESTED LIST ITERATOR'''
# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
# Implement the NestedIterator class:
#     - NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
#     - int next() Returns the next integer in the nested list.
#     - boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:
#     - initialize iterator with nestedList
#     - res = []
#     - while iterator.hasNext()
#         - append iterator.next() to the end of res
#     - return res
# If res matches the expected flattened list, then your code will be judged as correct.

# Example 1:
#     Input: nestedList = [[1,1],2,[1,1]]
#     Output: [1,1,2,1,1]
#     Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
#     Input: nestedList = [1,[4,[6]]]
#     Output: [1,4,6]
#     Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

# Constraints:
#     1 <= nestedList.length <= 500
#     The values of the integers in the nested list is in the range [-106, 106].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Create empty list to store flattened integers
        self.flatten_list = []

        # Recusive function to flatten nested structure
        def flatten(nested_list):
            for item in nested_list:
                if item.isInteger():
                    self.flatten_list.append(item.getInteger())
                else:
                    flatten(item.getList())
        
        # Start the flattening process
        flatten(nestedList)
        
        # Initialize the current index for iterating through the flattened list
        self.current_index = 0
    
    def next(self) -> int:
        # Return next integer and move index forward
        val = self.flatten_list[self.current_index]
        self.current_index += 1
        return val
    
    def hasNext(self) -> bool:
        # Check if there are more elements in flattened list
        return self.current_index < len(self.flatten_list)

'''FIND MEDIAN FROM DATA STREAM'''
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#     - For example, for arr = [2,3,4], the median is 3.
#     - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#     - MedianFinder() initializes the MedianFinder object.
#     - void addNum(int num) adds the integer num from the data stream to the data structure.
#     - double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
#     Input
#         ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
#         [[], [1], [2], [], [3], []]
#     Output
#         [null, null, null, 1.5, null, 2.0]
#     Explanation
#         MedianFinder medianFinder = new MedianFinder();
#         medianFinder.addNum(1);    // arr = [1]
#         medianFinder.addNum(2);    // arr = [1, 2]
#         medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
#         medianFinder.addNum(3);    // arr[1, 2, 3]
#         medianFinder.findMedian(); // return 2.0

# Constraints:
#     -105 <= num <= 105
#     There will be at least one element in the data structure before calling findMedian.
#     At most 5 * 104 calls will be made to addNum and findMedian.
 
# Follow up:
#     If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
#     If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinder:

    def __init__(self):
        self.min_heap = []  # Heap for larger half of numbers
        self.max_heap = []  # Heap for smaller half of numbers

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the heaps if necessary
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]