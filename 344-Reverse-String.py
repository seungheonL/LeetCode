from typing import *


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i, char in enumerate(s):
            if i < len(s) / 2:
                temp = s[i]
                s[i] = s[len(s) - 1 - i]
                s[len(s) - 1 - i] = temp
