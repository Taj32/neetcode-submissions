class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge case
        if len(s) == 0:
            return 0

        l = 0
        max_l = 0
        longestString = ""
        
        for char in s:
            index = longestString.find(char)
            if index != -1:
                print("repeat found")
                
                pre = longestString[:index] # includes char at index
                after = longestString[index+1:] #does not include char



                l = len(after) + 1 # reset length and add the 1 for current char
                longestString = after + char

            else:
                # add to the longest string
                l += 1
                print("base case (l + 1) = " + str(l))
                longestString = longestString + char

            if(l > max_l):
                    max_l = l
        
        if(l > max_l):
            max_l = l


        return max_l