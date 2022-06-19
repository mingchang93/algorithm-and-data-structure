from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        hash_map = defaultdict(list)
        for s in strs:
            hash_map[''.join(sorted(s))].append(s)

        return list(hash_map.values())