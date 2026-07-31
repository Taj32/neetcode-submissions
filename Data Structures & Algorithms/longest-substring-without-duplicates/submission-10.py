class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. declare variables
        char_set = set() # completely unique elements no repeats allowed
        l = 0
        maxl = 0 

        # iterate over r
        for r in range(len(s)):
            print(s[r])
            # 2. check for repetitions, if one exists shrink from the left until the repeat is removed
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            #3. add the new char
            char_set.add(s[r])

            #4. calculate the max
            maxl = max(maxl, r - l + 1)
        
        return maxl

# attempt 3 - charset (with claude that I looked at)