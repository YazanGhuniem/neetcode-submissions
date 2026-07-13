class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        for letter in s:
            s_map[letter]+=1
        for letter in t:
            t_map[letter]+=1
        if t_map == s_map:
            return True
        else:
            return False