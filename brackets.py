def is_balanced(expression):
    stack = []  # Initialize an empty stack to store opening brackets
    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}

    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        else:
            continue
    return not stack


balanced_expression = "[()]<{<>[()()]()}>"
unbalanced_expression = "[(])"

print(is_balanced(balanced_expression))
print(is_balanced(unbalanced_expression))
