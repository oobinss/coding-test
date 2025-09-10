n = int(input())
s = input()
cnt2 = s.count('2')
cnte = s.count('e')

if cnt2 > cnte:
    print('2')
elif cnt2 < cnte:
    print('e')
else:
    print('yee')
