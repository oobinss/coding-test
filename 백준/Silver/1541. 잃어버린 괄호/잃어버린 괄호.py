expression = input().strip()

parts = expression.split('-')

initial_sum = sum(map(int, parts[0].split('+')))

sub_sum = 0
for part in parts[1:]:
    sub_sum += sum(map(int, part.split('+')))

result = initial_sum - sub_sum

print(result)