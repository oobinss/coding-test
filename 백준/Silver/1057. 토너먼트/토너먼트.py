n, kim, lim = map(int, input().split())

round = 0

while kim != lim:
    kim = (kim + 1) // 2
    lim = (lim + 1) // 2
    round += 1
    
    
print(round)