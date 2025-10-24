N = int(input())
problems = {}

for _ in range(N):
    title, difficulty = input().split()
    problems[title] = int(difficulty)

sorted_problems = sorted(problems.items(), key=lambda x: x[1])

print(sorted_problems[0][0])
