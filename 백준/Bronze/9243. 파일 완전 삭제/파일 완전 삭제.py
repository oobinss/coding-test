n = int(input())
origin_file = input()
change_file = input()

if n % 2 == 0:
    expected = origin_file
else:
    expected = ''.join("1" if c == "0" else "0" for c in origin_file)
        
print("Deletion succeeded" if expected == change_file else "Deletion failed")