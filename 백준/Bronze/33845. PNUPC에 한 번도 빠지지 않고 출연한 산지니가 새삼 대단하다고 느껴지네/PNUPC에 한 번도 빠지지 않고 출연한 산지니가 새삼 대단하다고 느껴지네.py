S = input().strip()
T = input().strip()

remove_set = set(S)
result = ''.join(ch for ch in T if ch not in remove_set)
    
print(result)