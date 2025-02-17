5.17
def longest_valid_parentheses(s):
    stack = [-1]
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    s = input().strip()
    print(longest_valid_parentheses(s))
