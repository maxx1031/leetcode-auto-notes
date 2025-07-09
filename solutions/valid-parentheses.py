class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack:
                    return False
                top = stack.pop()
                if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                    return False