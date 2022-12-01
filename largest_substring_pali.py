def longestPalindrome(s: str) -> str:
        result = ""
        sub_lst = [s[i: j] for i in range(len(s))
          for j in range(i + 1, len(s) + 1)]
        # result = ""
        for i in sub_lst:
            k = i[::-1]
            if k in sub_lst and k == k[::-1] and len(k) > len(result):
                result = k
        return result
print(longestPalindrome("12215"))