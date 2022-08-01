# wrong answer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        seen = {}
        longestSub = s[0]
        prevLongestStr = s[0]
        seen[s[0]] = True
        for letter in range(1,len(s)):
            if s[letter] in seen:
                seen = {}
                if len(longestSub) > len(prevLongestStr): 
                    prevLongestStr = longestSub
                longestSub = s[letter]
                seen[s[letter]] = True
            else:
                longestSub += s[letter]
                seen[s[letter]] = True
        return max(len(prevLongestStr), len(longestSub))
