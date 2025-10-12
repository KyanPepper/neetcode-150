from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_lists = {}
        for str in strs:
            sortedstr = "".join(sorted(str))
            if sortedstr in anagram_lists:
                anagram_lists[sortedstr].append(str)
            else:
                anagram_lists[sortedstr] = [str]
        return list(anagram_lists.values())
                