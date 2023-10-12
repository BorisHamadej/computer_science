def numDecodings(s):
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        if 1 <= int(s[i - 1]) <= 9:
            dp[i] += dp[i - 1]
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


# Example usage:
s = "11106"
print(numDecodings(s))  # Output: 2 (AAJF and KJF are the two valid decodings)
