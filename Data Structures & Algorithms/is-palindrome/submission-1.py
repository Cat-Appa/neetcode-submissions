class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make every alphabet in the given string into all lowercase.
        s = s.lower()

        # initialize filtered array.
        filtered = []

        # apply filter
        for char in s:
            if char.isalnum():
                filtered.append(char)

        # initialize two pointer
        p1 = 0
        p2 = len(filtered) - 1

        # prevent pointer overlap/passing by.
        while p1 < p2:
            if filtered[p1] != filtered[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True