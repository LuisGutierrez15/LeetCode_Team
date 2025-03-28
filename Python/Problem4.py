class Problem4:
    def shortestPalindrome(self, s: str) -> str:
        if s.isspace() or s == "" or len(s) == 1:
            return s
        s_mirror: str = s[::-1]

        step: int = 0

        while True:
            test: str = s
            temp = s_mirror[:step]
            test = temp + test

            is_odd: bool = len(test) % 2 == 1
            plus: int = 1 if is_odd else 0

            if test[: len(test) // 2 + plus][::-1] == test[len(test) // 2 :]:
                return test

            step += 1


test: str = "abbacd"
expected: str = "dcabbacd"

p4: Problem4 = Problem4()


print(p4.shortestPalindrome(test))
