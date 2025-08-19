def toggle(state):
    return 1 - state

def main():
    n = int(input())  
    switches = list(map(int, input().split()))
    student_count = int(input())
    
    for _ in range(student_count):
        gender, num = map(int, input().split())
        
        if gender == 1:
            
            for i in range(num-1, n, num):
                switches[i] = toggle(switches[i])
                
        else:
            
            index = num - 1  

            left, right = index, index
            while left > 0 and right < n-1 and switches[left-1] == switches[right+1]:
                left -= 1
                right += 1
            
            for i in range(left, right+1):
                switches[i] = toggle(switches[i])

    for i in range(n):
        print(switches[i], end=' ')
        if (i+1) % 20 == 0:
            print()

if __name__ == "__main__":
    main()
