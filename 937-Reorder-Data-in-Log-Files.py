from typing import *


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        first = []
        second = []
        for log in logs:
            splited = log.split()
            if splited[1].isdigit():
                second.append(log)
            elif splited[1].isalpha():
                first.append(log)

        first.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return first + second
