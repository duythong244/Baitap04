def normalize_expression(expr):
    stack = []
    result = ""
    
    for char in expr:
        if char == '(':
            stack.append(result)
            result = ""
        elif char == ')':
            if stack:
                result = stack.pop() + result
        else:
            result += char
    
    return result

def are_expressions_equal(P1, P2):
    return normalize_expression(P1) == normalize_expression(P2)

# Input number of test cases
T = int(input("Enter number of test cases: "))
for _ in range(T):
    P1 = input().strip()
    P2 = input().strip()
    if are_expressions_equal(P1, P2):
        print("YES")
    else:
        print("NO")
