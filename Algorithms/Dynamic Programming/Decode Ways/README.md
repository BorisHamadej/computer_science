# Decode Ways

A message containing letters from A—Z can be encoded into numbers using the following
mapping:
To decode an encoded message, all the digits must be grouped then mapped back into
letters using the reverse of the mapping above (there may be multiple ways).

**Examples:**

```
"11106" can be mapped into:
• "AAJF" with the grouping (1 1 10 6)
• "KJF" with the grouping (11 10 6)
```

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into
since "6" is different from "06" .
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

### Python Program to decode ways

```python
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


s = "11106"
print(numDecodings(s))
```

**Output:**

```
2
```

This function uses dynamic programming to keep track of the number of ways to decode the string up to a certain index.
It iterates through the string, considering one-digit and two-digit substrings, and updates the dp array accordingly.
Finally, it returns dp[n], which represents the number of ways to decode the entire string.