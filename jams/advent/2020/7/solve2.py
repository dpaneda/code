import sys

bags = {}

for line in sys.stdin:
    data = line.split(" ")
    color = f"{data[0]} {data[1]}"
    data = data[4:]
    bags[color] = []
    while len(data) > 3:
        color2 = f"{data[1]} {data[2]}"
        bags[color].append((int(data[0]), color2))
        data = data[4:]

print(bags)

def count_bags(color):
    total_bags = 1
    for n, color in bags[color]:
        total_bags += n * count_bags(color)
    return total_bags

print(count_bags('shiny gold') - 1)
