from typing import List
from collections import defaultdict, deque

'''WORD LADDER'''
#     A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#     Every adjacent pair of words differs by a single letter.
#     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     sk == endWord
#     Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
#     Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#     Output: 5
#     Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:
#     Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
#     Output: 0
#     Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# Constraints:
#     1 <= beginWord.length <= 10
#     endWord.length == beginWord.length
#     1 <= wordList.length <= 5000
#     wordList[i].length == beginWord.length
#     beginWord, endWord, and wordList[i] consist of lowercase English letters.
#     beginWord != endWord
#     All the words in wordList are unique.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create a set for faster word lookup
        wordSet = set(wordList)
        
        # If the endWord is not in the wordList, there's no valid sequence
        if endWord not in wordSet:
            return 0
        
        # Create a graph where each node has its neighbors
        def construct_graph(wordSet):
            graph = defaultdict(list)
            for word in wordSet:
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    graph[pattern].append(word)
            return graph
        
        graph = construct_graph(wordSet)
        
        # BFS to find the shortest transformation sequence
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for neighbor in graph[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        return 0