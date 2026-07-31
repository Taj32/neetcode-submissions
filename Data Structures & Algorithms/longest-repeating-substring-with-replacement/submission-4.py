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

# attempt 2 - cleaner version with max_f
# - still got big o in the 2nd attempt but only because of the 26 char constaint
# - better to keep a running understanding of the max_frequency instead of rescanning the hashmap every iteration