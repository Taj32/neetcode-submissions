class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_elements = {}
        top_k = []

        # 1. iterate over the array and create the hashmap
        for num in nums:
            print(num)
            k_elements[num] = k_elements.get(num, 0) + 1

        # 2. sort the hashmap
        sorted_k_elements = dict(sorted(k_elements.items(), key=lambda item: item[1], reverse=True))
        print(sorted_k_elements)



        # 3. pick the top k of the hashmap
        for key, pair in sorted_k_elements.items():
            if(len(top_k) != k):
                top_k.append(key)
            else:
                break

        return top_k