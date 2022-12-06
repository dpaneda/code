import sys
import re

valids = 0

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

# Rules
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def validate(cp_fields):
    if not 1920 <= int(cp_fields['byr']) <= 2002:
        print('byr')
        return False
    if not 2010 <= int(cp_fields['iyr']) <= 2020:
        print('iyr')
        return False
    if not 2020 <= int(cp_fields['eyr']) <= 2030:
        print('eyr')
        return False
    hgt = cp_fields['hgt']
    d = int(hgt[:-2])
    if 'cm' in hgt:
        if not 150 <= d <= 193:
            print('hgt')
            return False
    elif 'in' in hgt:
        if not 59 <= d <= 76:
            print('hgt')
            return False
    else:
        print('hgt')
        return False
    if not re.match('^#[0-9a-f]{6}$', cp_fields['hcl']):
        print('hcl')
        return False
    if cp_fields['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        print('ecl')
        return False
    if not re.match('^\d{9}$', cp_fields['pid']):
        print('pid')
        return False
    
    return True

cp_fields = {}
for line in sys.stdin:
    line = line.strip()
    if line:
        for field in line.split(' '):
            k, v = field.split(':')
            cp_fields[k] = v
    else:
        # Validate
        print(cp_fields)
        try:
            if validate(cp_fields):
                valids += 1
        except Exception as e:
            print(e)
            pass
        cp_fields = {}

print(valids)
