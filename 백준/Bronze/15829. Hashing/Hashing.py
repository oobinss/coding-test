L = int(input())
s = input()
r = 31
M = 1234567891

hash_value = 0
for i in range(L):
    a = ord(s[i])-ord('a')+1
    hash_value += a * (r ** i )

print(hash_value % M)    
