from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        li1= []
        for char in s:
            if char.isalnum():
                li1.append(char.lower())
        li2 = []
        for i in range(len(li1)):
            li2.append(li1[len(li1) - 1 - i])
            
        return li1 == li2
            
            
            
        