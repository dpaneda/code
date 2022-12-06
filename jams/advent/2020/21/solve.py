import sys

all_ingredients = {}
all_allergens = {}

for line in sys.stdin:
    l = line.split(':')
    ingredients = l[0].split()
    allergens = l[1].split()
    for s in ingredients:
        all_ingredients[s] = all_ingredients.get(s, 0) + 1
    for a in allergens:
        if a not in all_allergens:
            all_allergens[a] = set(ingredients)
        else:
            all_allergens[a] &= set(ingredients)

# Resolve allergens
for _ in range(len(all_allergens)):
    for a, ing in all_allergens.items():
        if len(ing) == 1:
            ingredient = all_allergens[a].pop()
            for b in all_allergens:
                all_allergens[b].discard(ingredient)
            all_allergens[a].add(ingredient)

bad_ones = {}
for a, k in all_allergens.items():
    ingredient = k.pop()
    bad_ones[ingredient] = a

print(sum([v for k, v in all_ingredients.items() if k not in bad_ones.keys()]))

l = [k for k,_ in sorted(bad_ones.items(), key=lambda item: item[1])]
print(','.join(l))
