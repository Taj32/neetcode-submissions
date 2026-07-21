class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Check if none
        if s == None or t == None:
            return False
        
        s_hash = dict()
        t_hash = dict()
        # 1. iterate over the the strings
        for char in s:
            #check if the char already exists
            if char in s_hash:
                #append the pair
                s_hash[char] = s_hash[char] + 1
            else:
                s_hash[char] = 1
        
        for char in t:
            #check if the char already exists
            if char in t_hash:
                #append the pair
                t_hash[char] = t_hash[char] + 1
            else:
                t_hash[char] = 1

        
        print(s_hash)
        print(t_hash)
        return(s_hash == t_hash)
        
        


