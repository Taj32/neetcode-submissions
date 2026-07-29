class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None

        left = 0
        right = len(numbers) - 1

        # poninter loop
        while left < right:
            twoSum = numbers[left] + numbers[right]

            if(twoSum == target):
                return [left + 1, right + 1]
            elif(twoSum > target):
                right -= 1
            else:
                left += 1

        return None # Shouldnt run --> exactly one solution

# Attempt #2:
# Time: O(n) ; Space O(1)
# optimal solution :)