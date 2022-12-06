import sys

yes_count = 0
all_yes_count = 0

all_yes = set()
yes = set()

for line in sys.stdin:
    line = line.strip()
    if not yes:
        all_yes = set(line)
        yes = set(line)
    elif line:
        yes |= set(line)
        all_yes &= set(line)
    else:
        yes_count += len(yes)
        all_yes_count += len(all_yes)
        yes = set()

print(yes_count)
print(all_yes_count)
