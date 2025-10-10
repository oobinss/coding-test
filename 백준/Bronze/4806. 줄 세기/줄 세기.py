import sys

def count_lines():
    lines = sys.stdin.read().splitlines()
    print(len(lines))

count_lines()