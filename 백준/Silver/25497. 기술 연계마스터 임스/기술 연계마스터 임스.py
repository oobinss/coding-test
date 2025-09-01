N=int(input())

skill=list(str(input()))

num=0
used_list=[]

for i in skill :
    if (i=='L' or i=='S') :
        used_list.append(i)
    elif (i=='K') :
        if 'S' in used_list :
            used_list.remove('S')
            num=num+1
        else :
            break
    elif (i=='R') :
         if 'L' in used_list :
            used_list.remove('L')
            num=num+1
         else :
             break
    else :
         num=num+1

print(num)