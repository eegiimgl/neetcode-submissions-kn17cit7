class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash_str(_str):
            _hash = [0] * 26

            for ch in _str:
                _hash[ord(ch) - ord('a')] += 1

            return str(_hash)

        results = defaultdict(list)

        for _st in strs:
            results[hash_str(_st)].append(_st)


        return list(results.values())