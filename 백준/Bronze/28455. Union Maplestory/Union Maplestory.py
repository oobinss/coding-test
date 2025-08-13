N = int(input())
levels = [int(input()) for _ in range(N)]

levels.sort(reverse=True)

attack_levels = levels[:42]

level_sum = sum(attack_levels)

def get_bonus(level):
    bonus = 0
    if level >= 60:
        bonus += 1
    if level >= 100:
        bonus += 1
    if level >= 140:
        bonus += 1
    if level >= 200:
        bonus += 1
    if level >= 250:
        bonus += 1
    return bonus

stat_sum = sum(get_bonus(level) for level in attack_levels)

print(f"{level_sum} {stat_sum}")
