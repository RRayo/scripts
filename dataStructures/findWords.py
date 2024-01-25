# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]


from typing import List
from collections import defaultdict

class Solution:
    def charFrequency(self, input):
        if type(input) == str:
            freq_hash = defaultdict(int)
            for char in input:
                freq_hash[char] += 1
        elif type(input) == list:
            # save the positions of each char also
            freq_hash = {}
            for i in range(len(input)):
                for j in range(len(input[0])):
                    char = input[i][j]
                    if char not in freq_hash:
                        freq_hash[char] = [1, [[i,j]]]
                    else:
                        counter, positions = freq_hash[char]
                        positions.append([i,j])
                        freq_hash[char] = [counter+1, positions]
        return freq_hash
    
    def boardContainsChars(self, board_hash, word_hash):
        for char, frequency in word_hash.items():
            if char not in board_hash or frequency > board_hash[char][0]:
                return False
        return True
    
    def filterWords(self, words, words_hash, board_freq_hash):
        filtered_words = []
        for word in words:
            words_hash[word] = self.charFrequency(word)
            if self.boardContainsChars(board_freq_hash, words_hash[word]):
                filtered_words.append(word)
        return filtered_words
    
    def boardContainsWord(self, board, board_freq_hash, word):
        board_height = len(board)
        board_width = len(board[0])
        # check the first char of the word and traverse the board looking for the next chars
            #   create a set of visited coordinates and a queue(FIFO) for the next coordinates to visit
            #   if a path doesn't continue revert the visited coords in the set until that point
        partial_word = word[0]
        first_char_coord = board_freq_hash[word[0]][1]
        # add all 4 directions of the next coordinate to a queque, coordinates and word index
        #   add if the next position is inside the board and has the next char 
        path_queue = [[first_char_coord, 0, [first_char_coord]]]
        checked_coords = set()
        while partial_word != word and path_queue:
            current_coordinate, char_index, current_path = path_queue.pop()
            # check if word is completed
            if char_index == len(word)-1:
                return True
            
            next_char_index = char_index+1
            next_char = word[next_char_index]
            y_current, x_current = current_coordinate # row, col
            
            added_point = False
            # left
            #   check if exist in visited set also
            if x_current-1 >= 0 and [y_current, x_current-1] not in checked_coords and board[y_current][x_current-1] == next_char:
                current_path.append([y_current,x_current-1])
                path_queue.append([y_current,x_current-1], next_char_index, current_path)
                # add current to set of visited points
                checked_coords.add([y_current, x_current-1])
                added_point = True
            # right
            if x_current+1 < board_width and [y_current, x_current+1] not in checked_coords and board[y_current][x_current+1] == next_char:
                current_path.append([y_current,x_current+1])
                path_queue.append([y_current,x_current+1], next_char_index, current_path)
                # add current to set of visited points
                checked_coords.add([y_current, x_current+1])
                added_point = True
            # up
            if y_current-1 >= 0 and [y_current-1, x_current] not in checked_coords and board[y_current-1][x_current] == next_char:
                current_path.append([y_current-1,x_current])
                path_queue.append([y_current-1,x_current], next_char_index, current_path)
                # add current to set of visited points
                checked_coords.add([y_current-1, x_current])
                added_point = True
            # down
            if y_current+1 < board_height and [y_current+1, x_current] not in checked_coords and board[y_current+1][x_current] == next_char:
                current_path.append([y_current+1,x_current])
                path_queue.append([y_current+1,x_current], next_char_index, current_path)
                # add current to set of visited points
                checked_coords.add([y_current+1, x_current])
                added_point = True
            # if none can add a next element -> remove path of searched nodes of the set
            if not added_point:
                checked_coords.remove([y_current, x_current])

        return False
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # check if all letters of the word exist in the matrix
        #   create a hash with the frequency of the matrix words
        #   for each word create his hash and compare it to the matrix, if not included freq_word <= freq_matrix, continue
        result = []
        board_freq_hash = self.charFrequency(board)
        words_hash = {}
        filtered_words = self.filterWords(words, words_hash, board_freq_hash)

        for word in filtered_words:
            if self.boardContainsWord(board, board_freq_hash, word):
                result.append(word)

        return filtered_words
        # return result


s = Solution()

cases = [

    [[[["o","a","a","n"],
       ["e","t","a","e"],
       ["i","h","k","r"],
       ["i","f","l","v"]],["oath","pea","eat","rain"]], ["eat","oath"]]
]

for input, expected in cases:
    matrix, words = input
    result = s.findWords(matrix, words)
    print(result == expected, input, result, expected)