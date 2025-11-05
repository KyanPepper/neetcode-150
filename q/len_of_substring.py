class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}  # char -> last index
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1  # jump left past the previous duplicate
            last_seen[ch] = right
            best = max(best, right - left + 1)

        return best
