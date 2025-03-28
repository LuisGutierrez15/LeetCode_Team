import time


class Problem3:
    def shortestPalindrome(self, s: str) -> str:
        if s.isspace() or s == "":
            return s
        # Quick thinking
        # the length of the result string is always odd

        # Correction, is not always odd

        # Step 1: mirror the word
        s_mirror: str = s[::-1]
        # Step 2: add a letter from original s until the total length is odd and half of s is equal to the other half

        i: int = 0
        trying: int = 1

        while (
            s_mirror[: len(s_mirror) // 2 + 1][::-1] != s_mirror[len(s_mirror) // 2 :]
        ):
            try:
                s_mirror += s[i]
                i += 1
            except:
                s_mirror = s[::-1]
                i = trying
                trying += 1

        print(s_mirror[: len(s_mirror) // 2])
        print(s_mirror[len(s_mirror) // 2 :])
        return s_mirror


test: str = "abbacd"
expected: str = "dcabbacd"

p3: Problem3 = Problem3()
print(p3.shortestPalindrome(test))
