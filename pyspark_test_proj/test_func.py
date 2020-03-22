import numpy as np


def string_match_percentage(s, t):
    global row, col
    rows = len(s) + 1
    cols = len(t) + 1
    distance = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 2
            distance[row][col] = min(distance[row - 1][col] + 1,
                                     distance[row][col - 1] + 1,
                                     distance[row - 1][col - 1] + cost)
    # if ratio_calc:
    match_percentage = ((len(s) + len(t)) - distance[row][col]) / (len(s) + len(t)) * 100
    if match_percentage > 58:
        return True
    else:
        return False
    # else:
    #
    #     return "The strings are {} edits away".format(distance[row][col])


Str1 = "gyu"
Str2 = "agcsallianz"
Ratio = string_match_distance(Str1, Str2)
print(Ratio)
