from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # 2 dictionary approach
        need = Counter(t)
        need_count = len(need)          # distinct characters that must be satisfied
        window_count = defaultdict(int)
        have = 0                        # distinct characters currently satisfied

        l = 0
        best_len = float('inf')
        best_l, best_r = 0, 0

        for r in range(len(s)):
            c = s[r]
            window_count[c] += 1
            if c in need and window_count[c] == need[c]:
                have += 1

            while have == need_count:                    # window is fully valid — try to shrink
                if (r - l + 1) < best_len:
                    best_len = r - l + 1
                    best_l, best_r = l, r # current window is smaller than the global so adjust 

                window_count[s[l]] -= 1 # reduce the window items in 
                if s[l] in need and window_count[s[l]] < need[s[l]]: # check if the shrink the validity
                    have -= 1                             # shrinking broke validity for this char
                l += 1 

        return s[best_l:best_r+1] if best_len != float('inf') else ""

    # claude fix - O(n + m) time, o(1) space - where m = len(t), n = len(s)
    # -- 