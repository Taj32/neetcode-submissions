class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))   # canonical form "eat" --> ('a','e','t') ; "tea" --> ('a','e','t')
            groups[key].append(s)
        return list(groups.values())
    
     