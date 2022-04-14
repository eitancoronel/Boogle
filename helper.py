
def checking_board_size(board):
    """
    This function check the board size
    :param board:
    :return:
    """
    x, y = len(board), len(board[0])
    board_size = (x, y)
    return board_size


def path_helper(board_size, path, board):
    """
    this function iterates over the path and return None if he not 'legal' (we are also calling the function
    illegal_jump
    :param board_size: the size of the board
    :param path: the path we wants to check
    :return:curr or None depending if the the path is valid
    """
    checked = []
    curr = ""
    for i, tup in enumerate(path):
        if tup in checked:
            return None
        if board_size[0] - tup[0] <= 0 or board_size[1] - tup[1] <= 0:
            return None
        if i > 0:
            if illegal_jump(path[i - 1], tup, board_size):
                return None
        checked.append(tup)
        curr += board[tup[0]][tup[1]]
    return curr


def is_valid_path(board, path, words):
    """
    checks if the function is a valid path
    :param board: the board
    :param path: the path
    :param words: the words
    :return: None or curr
    """
    board_size = checking_board_size(board)
    curr = path_helper(board_size,path,board)
    if curr is None:
        return None
    if curr in words:
        return curr
    return None


def illegal_jump(pos1, pos2, board_size):
    """
    cheks if we are doing illegal jumps
    :return: True or False dipanding if the jump is legal or not.
    """
    if board_size[0] - pos1[0] <= 0 or board_size[1] - pos1[0] <= 0:
        return True
    if board_size[0] - pos2[0] <= 0 or board_size[1] - pos2[0] <= 0:
        return True
    if abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1 and pos1 != pos2:
        return False
    return True


def find_length_n_paths(n, board, words):
    """
    this function will iterate over the list of path that we have and append them to a list if they are valid
    :param board: the board
    :param words: the words
    :param result: an empty list that we will append the valid path
    :return: the list with all the valid path of a len n
    """
    board_size = checking_board_size(board)
    lst = []
    result = []
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            final = []
            helper_paths(n, board_size[0], board_size[1], final, [(i, j)])
            lst.extend(final)
    for i in lst:  # iterates over lst of paths
        check = is_valid_path(board, i, words)
        if check is not None:
            result.append(i)
    return result

def helper_paths(n, x, y, final, curr):
    """ this functions calls all the different possible path"""
    if len(curr) == n:
        final.append(curr)
        return
    var = curr[-1]
    helper_paths_up(var, curr, n, x, y, final)
    helper_paths_down(var, curr, n, x, y, final)
    helper_paths_left(var, curr, n, x, y, final)
    helper_paths_right(var, curr, n, x, y, final)
    helper_paths_up_left(var, curr, n, x, y, final)
    helper_paths_up_right(var, curr, n, x, y, final)
    helper_paths_down_left(var, curr, n, x, y, final)
    helper_paths_down_right(var, curr, n, x, y, final)
    return

def helper_paths_up(var,curr,n, x, y, final):
    """path going up"""
    if 0 <= var[0] - 1 < x:  # up
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1]))
        helper_paths(n, x, y, final, curr_1)


def helper_paths_down(var,curr,n, x, y, final):
    """path going down"""
    if 0 <= var[0] + 1 < x:  # down
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1]))
        helper_paths(n, x, y, final, curr_1)


def helper_paths_left(var, curr, n, x, y, final):
    """path going left"""
    if 0 <= var[1] - 1 < y:  # left
        curr_1 = curr[:]
        curr_1.append((var[0], var[1] - 1))
        helper_paths(n, x, y, final, curr_1)


def helper_paths_right(var, curr, n, x, y, final):
    """path going right"""
    if 0 <= var[1] + 1 < y:  # right
        curr_1 = curr[:]
        curr_1.append((var[0], var[1] + 1))
        helper_paths(n, x, y, final, curr_1)


def helper_paths_up_left(var, curr, n, x, y, final):
    """path going up left"""
    if 0 <= var[0] - 1 < x and 0 <= var[1] - 1 < y:  # up - left
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1] - 1))
        helper_paths(n, x, y, final, curr_1)


def helper_paths_up_right(var, curr, n, x, y, final):
    """path going up right"""
    if 0 <= var[0] - 1 < x and 0 <= var[1] + 1 < y:  # up - right
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1] + 1))
        helper_paths(n, x, y, final, curr_1)


def helper_paths_down_left(var, curr, n, x, y, final):
    """path going down left"""
    if 0 <= var[0] + 1 < x and 0 <= var[1] - 1 < y:  # down - left
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1] - 1))
        helper_paths(n, x, y, final, curr_1)


def helper_paths_down_right(var, curr, n, x, y, final):
    """path going down right"""
    if 0 <= var[0] + 1 < x and 0 <= var[1] + 1 < y:  # down - right
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1] + 1))
        helper_paths(n, x, y, final, curr_1)


def find_length_n_words(n, board, words):
    """
    this function find the words that we have
    and will iterate of the list of all the possible path .
    :return: list of all the result
    """
    board_size = checking_board_size(board)
    lst = []
    result = []
    if check_no_words(n, words):
        return []
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            final = []
            helper_words(n, board_size[0], board_size[1], final, [(i, j)], board[i][j], board)
            lst.extend(final)
    for i in lst:  # iterates over lst of paths
        check = is_valid_path(board, i, words)
        if check is not None:
            result.append(i)
    return result

def helper_words(n, x, y, final, curr, curr_word, board):
    """this function take all the words with a len of n"""
    if len(curr_word) == n:
        final.append(curr)
        return
    if len(curr_word) > n:
        return
    var = curr[-1]
    helper_words_up(n, x, y, final, curr, curr_word, board, var)
    helper_words_down(n, x, y, final, curr, curr_word, board, var)
    helper_words_left(n, x, y, final, curr, curr_word, board, var)
    helper_words_right(n, x, y, final, curr, curr_word, board, var)
    helper_words_up_left(n, x, y, final, curr, curr_word, board, var)
    helper_words_up_right(n, x, y, final, curr, curr_word, board, var)
    helper_words_down_left(n, x, y, final, curr, curr_word, board, var)
    helper_words_down_right(n, x, y, final, curr, curr_word, board, var)
    return

def check_no_words(n, words):
    """
    :return: this function returns a boolean
    """
    bol = True
    for i in words:
        if len(i) == n:
            bol = False
    return bol


def helper_words_up(n, x, y, final, curr, curr_word, board,var):
    """words going up"""
    if 0 <= var[0] - 1 < x:  # up
        word_1 = curr_word
        word_1 += board[var[0] - 1][var[1]]
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1]))
        helper_words(n, x, y, final, curr_1, word_1, board)


def helper_words_down(n, x, y, final, curr, curr_word, board,var):
    """words going down """
    if 0 <= var[0] + 1 < x:  # down
        word_1 = curr_word
        word_1 += board[var[0] + 1][var[1]]
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1]))
        helper_words(n, x, y, final, curr_1, word_1, board)


def helper_words_left(n, x, y, final, curr, curr_word, board,var):
    """words going left"""
    if 0 <= var[1] - 1 < y:  # left
        word_1 = curr_word
        word_1 += board[var[0]][var[1] - 1]
        curr_1 = curr[:]
        curr_1.append((var[0], var[1] - 1))
        helper_words(n, x, y, final, curr_1, word_1, board)


def helper_words_right(n, x, y, final, curr, curr_word, board,var):
    """words going right"""
    if 0 <= var[1] + 1 < y:  # right
        word_1 = curr_word
        word_1 += board[var[0]][var[1] + 1]
        curr_1 = curr[:]
        curr_1.append((var[0], var[1] + 1))
        helper_words(n, x, y, final, curr_1, word_1, board)


def helper_words_up_left(n, x, y, final, curr, curr_word, board,var):
    """words going up left"""
    if 0 <= var[0] - 1 < x and 0 <= var[1] - 1 < y:  # up - left
        word_1 = curr_word
        word_1 += board[var[0] - 1][var[1] - 1]
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1] - 1))
        helper_words(n, x, y, final, curr_1, word_1, board)


def helper_words_up_right(n, x, y, final, curr, curr_word, board,var):
    """words going up right"""
    if 0 <= var[0] - 1 < x and 0 <= var[1] + 1 < y:  # up - right
        word_1 = curr_word
        word_1 += board[var[0] - 1][var[1] + 1]
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1] + 1))
        helper_words(n, x, y, final, curr_1, word_1, board)


def helper_words_down_left(n, x, y, final, curr, curr_word, board,var):
    """words going down left"""
    if 0 <= var[0] + 1 < x and 0 <= var[1] - 1 < y:  # down - left
        word_1 = curr_word
        word_1 += board[var[0] + 1][var[1] - 1]
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1] - 1))
        helper_words(n, x, y, final, curr_1, word_1, board)


def helper_words_down_right(n, x, y, final, curr, curr_word, board,var):
    """words going down right"""
    if 0 <= var[0] + 1 < x and 0 <= var[1] + 1 < y:  # down - right
        word_1 = curr_word
        word_1 += board[var[0] + 1][var[1] + 1]
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1] + 1))
        helper_words(n, x, y, final, curr_1, word_1, board)


def load_words_lst(file_path):
    """
    this function open the file wich contains the list of all the words
    :param file_path: the path to find the file
    :return:
    """
    with open(file_path, 'r') as stop_words:
        lineas = [linea.strip() for linea in stop_words]
    return lineas


def max_score_paths_helper(my_dict, final):
    """helper of the max score function , it will iterate over the values of my dict"""
    for i in my_dict.values():
        final.append(i[0])


def max_score_paths(board, words):
    """ this function has the responsibility to find the path that will give the maximum score"""
    board_size = checking_board_size(board)
    my_dict = {}
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            my_dict_new = helper_max_score(getmax(words), board_size[0], board_size[1],
                                           [(i, j)], board[i][j], board, my_dict, words)
            for t in my_dict_new:
                if t in my_dict:
                    if my_dict_new[t][1] >= my_dict[t][1]:
                        my_dict[t] = my_dict_new[t]
                else:
                    my_dict[t] = my_dict_new[t]
    final = []
    max_score_paths_helper(my_dict, final)
    return final


def helper_max_score(n, x, y, curr, curr_word, board, my_dict, words):
    """
    this is a helper to calculate the maximum score possible
    :param n:
    :param x , y : boarders of the board
    :param curr: the current item
    :param curr_word: the current word
    :param board: the board
    :param my_dict: the dictionnary
    :param words: the words
    :return: my dict
    """
    if len(curr) <= n and is_valid_path(board, curr, words):
        if curr_word not in my_dict:
            my_dict[curr_word] = (curr, len(curr) ** 2)
        else:
            if len(curr) ** 2 >= my_dict[curr_word][1]:
                my_dict[curr_word] = (curr, len(curr) ** 2)
    if len(curr) > n:
        return my_dict
    var = curr[-1]
    max_score_up(var, curr, n, x, y, curr_word, board, my_dict, words)
    max_score_down(var, curr, n, x, y, curr_word, board, my_dict, words)
    max_score_left(var, curr, n, x, y, curr_word, board, my_dict, words)
    max_score_right(var, curr, n, x, y, curr_word, board, my_dict, words)
    max_score_up_left(var, curr, n, x, y, curr_word, board, my_dict, words)
    max_score_up_right(var, curr, n, x, y, curr_word, board, my_dict, words)
    max_score_down_left(var, curr, n, x, y, curr_word, board, my_dict, words)
    max_score_down_right(var, curr, n, x, y, curr_word, board, my_dict, words)
    return my_dict


def getmax(words):
    """go over all the words and take the one that is the longest"""
    curr = 0
    for i in words:
        if len(i) >= curr:
            curr=len(i)
    return curr


def max_score_up(var,curr,n, x, y, curr_word, board, my_dict, words):
    """the max score in the direction up"""
    if 0 <= var[0] - 1 < x and (var[0] - 1, var[1]) not in curr:  # up
        word_1 = curr_word
        word_1 += board[var[0] - 1][var[1]]
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1]))
        helper_max_score(n, x, y, curr_1, word_1, board, my_dict, words)


def max_score_down(var,curr,n, x, y, curr_word, board, my_dict, words):
    """the max score in the direction down"""
    if 0 <= var[0] + 1 < x and (var[0] + 1, var[1]) not in curr:  # down
        word_1 = curr_word
        word_1 += board[var[0] + 1][var[1]]
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1]))
        helper_max_score(n, x, y, curr_1, word_1, board, my_dict, words)


def max_score_left(var,curr,n, x, y, curr_word, board, my_dict, words):
    """the max score in the direction left"""
    if 0 <= var[1] - 1 < y and (var[0], var[1] - 1) not in curr:  # left
        word_1 = curr_word
        word_1 += board[var[0]][var[1] - 1]
        curr_1 = curr[:]
        curr_1.append((var[0], var[1] - 1))
        helper_max_score(n, x, y, curr_1, word_1, board, my_dict, words)


def max_score_right(var,curr,n, x, y, curr_word, board, my_dict, words):
    """the max score in the direction right"""
    if 0 <= var[1] + 1 < y and var[1] + 1 < y and (var[0], var[1] + 1) not in curr:  # right
        word_1 = curr_word
        word_1 += board[var[0]][var[1] + 1]
        curr_1 = curr[:]
        curr_1.append((var[0], var[1] + 1))
        helper_max_score(n, x, y, curr_1, word_1, board, my_dict, words)


def max_score_up_left(var,curr,n, x, y, curr_word, board, my_dict, words):
    """the max score in the direction up left"""
    if 0 <= var[0] - 1 < x and 0 <= var[1] - 1 < y and (var[0] - 1, var[1] - 1) not in curr:  # up - left
        word_1 = curr_word
        word_1 += board[var[0] - 1][var[1] - 1]
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1] - 1))
        helper_max_score(n, x, y, curr_1, word_1, board, my_dict, words)


def max_score_up_right(var,curr,n, x, y, curr_word, board, my_dict, words):
    """the max score in the direction up right"""
    if 0 <= var[0] - 1 < x and 0 <= var[1] + 1 < y and (var[0] - 1, var[1] + 1) not in curr:  # up - right
        word_1 = curr_word
        word_1 += board[var[0] - 1][var[1] + 1]
        curr_1 = curr[:]
        curr_1.append((var[0] - 1, var[1] + 1))
        helper_max_score(n, x, y, curr_1, word_1, board, my_dict, words)


def max_score_down_left(var, curr,n, x, y, curr_word, board, my_dict, words):
    """the max score in the direction down left"""
    if 0 <= var[0] + 1 < x and 0 <= var[1] - 1 < y and (var[0] + 1, var[1] - 1) not in curr:  # down - left
        word_1 = curr_word
        word_1 += board[var[0] + 1][var[1] - 1]
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1] - 1))
        helper_max_score(n, x, y, curr_1, word_1, board, my_dict, words)


def max_score_down_right(var,curr,n, x, y, curr_word, board, my_dict, words):
    """the max score in the direction down right"""
    if 0 <= var[0] + 1 < x and 0 <= var[1] + 1 < y and (var[0] + 1, var[1] + 1) not in curr:  # down - right
        word_1 = curr_word
        word_1 += board[var[0] + 1][var[1] + 1]
        curr_1 = curr[:]
        curr_1.append((var[0] + 1, var[1] + 1))
        helper_max_score(n, x, y, curr_1, word_1, board, my_dict, words)