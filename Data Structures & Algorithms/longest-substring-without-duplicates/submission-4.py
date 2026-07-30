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
                print("---------------------")
                print(longestString)
                print("repeat found")
                print(index)
                pre = longestString[:index]
                after = longestString[index+1:]
                print("pre: " + pre)
                print("after: " + after)


                l = len(after) + 1
                longestString = after + char
                print("new longest string = " + longestString)

                # reset and continue
                if(l > max_l):
                    max_l = l
                
                print("----------------------")
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