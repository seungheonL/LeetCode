import collections
from typing import *


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = paragraph.split()
        result = []
        for word in words:
            flag = False
            for i in range(len(word)):
                s = word[i]
                if(s == '!' or s == '?' or s == ',' or s == "'"
                   or s == ';' or s == '.'):
                    result.append(word[:i])
                    flag = True
                    break
            if not flag:
                result.append(word)

        result = [x for x in result if x not in banned]

        m = collections.defaultdict(int)

        for v in result:
            m[v] += 1

        return max(m, key=m.get)
