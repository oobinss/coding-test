def java_equals(a, b):
    if a is None:
        return "NullPointerException"
    return str(a) == str(b)

def java_equals_ignore_case(a, b):
    if a is None:
        return "NullPointerException"
    # None도 lower 불가 -> 대조 결과 False
    if b is None:
        return False
    return str(a).lower() == str(b).lower()

A = input().strip()
B = input().strip()

A_py = None if A == "null" else A
B_py = None if B == "null" else B

result1 = java_equals(A_py, B_py)
result2 = java_equals_ignore_case(A_py, B_py)

print(result1 if result1 == "NullPointerException" else str(result1).lower())
print(result2 if result2 == "NullPointerException" else str(result2).lower())
