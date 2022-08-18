from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def getPalindrome(mid):
            left = mid
            right = mid + 1

            while 0 <= left and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1

            left += 1
            right -= 1
            result = s[left:right+1]

            left = mid
            right = mid + 2

            while 0 <= left and right < len(s):

                if s[left] != s[right]:
                    break
                left -= 1
                right += 1

            left += 1
            right -= 1
            result = max(result, s[left:right+1], key=len)

            return result

        answer = ''

        for i in range(len(s) - 1):
            answer = max(answer, getPalindrome(i), key=len)

        return answer


print(Solution().longestPalindrome(s="abb"))
