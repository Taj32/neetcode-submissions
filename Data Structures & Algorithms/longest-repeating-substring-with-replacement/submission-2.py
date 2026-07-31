class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #1. declare variables
        count = {}
        l = 0
        maxl = 0

        for r in range(len(s)):
            # increase the right 
            print(s[r])
            count[s[r]] = count.get(s[r], 0) + 1
            windowlength = r - l + 1
            mostFrequent = max(count, key=count.get)

            if ((windowlength - count[mostFrequent]) > k):
                # shrink left
                count[s[l]] -= 1
                l += 1
            
            #increase right

            # 4. get the max 
            maxl = max(maxl, r - l + 1)

            
        
        return maxl