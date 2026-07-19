class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)
        for wrd in strs:
            sorted_wrd = "".join(sorted(wrd))
            strings[sorted_wrd].append(wrd)

        return list(strings.values())
            
            