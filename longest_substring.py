class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = dict()
        start = 0
        max_len = 0
        max_subs = ""

        for i, ch in enumerate(s):
            if s[i] in last_seen and last_seen[s[i]] >= start:
                start = last_seen[s[i]] + 1

            last_seen[ch] = i
            current_window_length = i-start+1
            if current_window_length > max_len:
                max_len = i-start+1
                max_sub = s[start:i+1]
        print (last_seen, max_sub, max_len)        
        return max_len
    
    
Solution().lengthOfLongestSubstring("ppwkewwfgcvpsq")
    