class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        for chars in s:
            if chars in "{([":
                stack.append(chars)
            else:
                if not stack:
                    return False
                if stack.pop()!=pairs[chars]:
                    return False
        return not stack
        