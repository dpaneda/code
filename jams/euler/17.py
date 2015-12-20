#!/usr/bin/env python3

basicnumber = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
  "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", 
  "nineteen"]
  
twodigits = [0, 0, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def print_and_len(s):
  print(s)
  return len(s.replace(" ",""))

s = 0

for i in range(1, 1000):
  cents = int(i / 100)
  tens = int((i % 100) / 10)
  if tens > 1:
    rest = i - 100 * cents - 10 * tens
  else:
    rest = i - 100 * cents
    

  number = ""

  if cents:
    number += basicnumber[cents]
    number += " hundred "
    if rest or tens:
      number += "and "

  if tens > 1:
    number += twodigits[tens]
    number += " "

  number += basicnumber[rest]
  s += print_and_len(number)

s += len("onethousand")

print(s)
