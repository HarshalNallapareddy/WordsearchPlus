def solve(word_board, word_list):
    rows = len(word_board)
    cols = len(word_board[0])

    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    word_coords = []
    for word in word_list:
        for x in range(rows):
            for y in range(cols):
                if word_board[x][y] == word[0]:
                    for dir in directions:
                        temp_coords = [(x, y)]
                        build = word_board[x][y]
                        row = x
                        col = y
                        for i in range(1, len(word)):
                            row += dir[0]
                            col += dir[1]
                            if (row >= 0 and col >= 0 and row < rows and col < cols):
                                if (word_board[row][col] == word[i]):
                                    temp_coords.append((row, col))
                                    build += word[i]
                        if build == word:
                            word_coords += temp_coords
                            print(build)
                            break
    
    return word_coords 