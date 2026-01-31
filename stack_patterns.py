# Valid Parentheses using Stack
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)

    return not stack

print(is_valid_parentheses("()[]{}"))
print(is_valid_parentheses("(]"))
