from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for word in strs:
            original = word
            changed = ''.join(sorted(word))

            if changed in m:
                m[changed].append(original)
            else:
                m[changed] = [original]

        result = []

        for value in m.values():
            result.append(value)

        return result


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
