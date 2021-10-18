def minDistacne(word1, word2):
    # word1 -> laid horizontally
    # word2 -> laid vertically

    dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

    for row in range(len(word2) + 1):
        for col in range(len(word1) + 1):
            if row == 0:
                dp[row][col] = col
            elif col == 0:
                dp[row][col] = row
            elif word2[row - 1] == word1[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = 1 + min(
                    dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]
                )
    return dp[len(word2)][len(word1)]


if __name__ == "__main__":
    a = minDistacne("shep", "shepherdsville")
    print(a)
    # после слово shep 9 букв и выводится 9 букв