class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first thing we do is add all the words in the list to a dictionary
        Adict = defaultdict(list)
        for word in strs:
            sort_word = "".join(sorted(word))
            Adict[sort_word].append(word)
        return list(Adict.values())
            

            