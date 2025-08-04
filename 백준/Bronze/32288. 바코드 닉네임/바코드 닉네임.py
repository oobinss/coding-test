n = int(input())
S = input()
result = ""

for i in S:
    if(i == "l"):
        result += "L"
    else:
        result += "i"
    
print(result)