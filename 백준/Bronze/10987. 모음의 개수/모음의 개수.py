word = input()
aeiou = ["a", "e", "i", "o", "u"]

result = 0
for c in word:
    if c in aeiou:
        result += 1
        
print(result)
    