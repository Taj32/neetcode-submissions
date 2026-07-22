class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        result = []

        for index, num in enumerate(nums):
            difference = target - num
            if not hashMap:
                hashMap[index] = (difference)
            else:
                # check if there exists a difference value that is equal to current num
                if num in hashMap.values():
                    matching_key = None
                    for key, val in hashMap.items():
                        if val == num:
                            matching_key = key
                            break  # Stop searching after the first match
                    #pair found
                    result.append(matching_key)
                    result.append(index)
                    return result
                else:
                    #Add to the hash map
                    hashMap[index] = (difference)
            print(index)
        
        return result