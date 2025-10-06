class Solution(object):
    
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s):

        length = len(s)
        last_seen = set()
        subs = ""
        
        for i in range(length):
            for j in range(i, length):
                sub = s[i:j+1]
                if sub not in last_seen:
                    last_seen.add(sub)
                    if self.is_palindrome(sub) and len(sub) > len(subs):
                        subs = sub          
        return subs
        
print (Solution().longestPalindrome("babad"))




# class Solution(object):
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""

#         start = 0
#         end = 0

#         def expand_from_center(left, right):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return right - left - 1  # length of palindrome

#         for i in range(len(s)):
#             len1 = expand_from_center(i, i)       # odd-length center
#             len2 = expand_from_center(i, i + 1)   # even-length center
#             max_len = max(len1, len2)

#             if max_len > (end - start + 1):
#                 start = i - (max_len - 1) // 2
#                 end = i + max_len // 2

#         return s[start:end + 1]
