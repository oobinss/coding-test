num = 0
max_num = 0

for _ in range(10):
    out_train, in_train = map(int, input().split())
    num += in_train - out_train
    max_num = max(max_num, num)
    
print(max_num)
    