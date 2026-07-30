class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False


        # setting hte arrays
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # track how many letters have the same count in both arrays
        matches = sum(1 for i in range(26) if s1_count[i] == s2_count[i])


        # Sliding window one character at a time
        l = 0
        for r in range(len(s1), len(s2)):
            # edge case: all are the same a-z
            if matches == 26:
                return True

            
            # add the new right-side character
            idx_r = ord(s2[r]) - ord('a')
            s2_count[idx_r] += 1
            if s2_count[idx_r] == s1_count[idx_r]:
                matches += 1
            elif s2_count[idx_r] == s1_count[idx_r] + 1:
                matches -= 1

            # remove the outgoing left-side character
            idx_l = ord(s2[l]) - ord('a')
            s2_count[idx_l] -= 1
            if s2_count[idx_l] == s1_count[idx_l]:
                matches += 1
            elif s2_count[idx_l] == s1_count[idx_l] - 1:
                matches -= 1
            l += 1

        return matches == 26