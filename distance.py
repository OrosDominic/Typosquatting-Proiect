
KEYBOARD = ("qwertyuiop", "asdfghjkl", "zxcvbnm")

POSITIONS = {}

for r, row in enumerate(KEYBOARD):
    for c, letter in enumerate(row):
        POSITIONS[letter] = (r, c)


def cost_inlocuire(a, b, qwerty):
    if a == b:
        return 0

    if qwerty and a in POSITIONS and b in POSITIONS:
        r1, c1 = POSITIONS[a]
        r2, c2 = POSITIONS[b]

        if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1:
            return 0.5

    return 1


def distanta(a, b, qwerty=False):
    n, m = len(a), len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1]
                + cost_inlocuire(a[i - 1], b[j - 1], qwerty)
            )

            if (i > 1 and j > 1
                and a[i - 1] == b[j - 2]
                and a[i - 2] == b[j - 1]):
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

    return dp[n][m]

def damerau_levenshtein(a, b):
    return distanta(a, b)


def keyboard_distance(a, b):
    return distanta(a, b, True)
