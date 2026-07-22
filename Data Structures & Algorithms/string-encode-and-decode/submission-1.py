class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString = encodedString + "seperation" + string # example: _a_b_c

        encodedString = encodedString[::-1] # _a_b_c ---> c_b_a
        
        print("end result of encoding: " + encodedString)
        return encodedString

    def decode(self, s: str) -> List[str]:
        # input c_b_a
        print("decode input:" + s)

        # reverse the input
        s = s[::-1] # c_b_a ---> _a_b_c --->
        print("decode reversed: " + s)
        key = "seperation"
        # seperate the strs
        result = []
        result = s.split(key) # result: ['a', 'b', 'c']
        print("decode results: " + str(result))
        return result[1:]


