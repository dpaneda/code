
line = readline(STDIN)
parsed_line = split(line, ", ")

n = int(parsed_line[1])

rules = Dict()

for rule in parsed_line[2:end]
  parts = split(rule, "->")
  c = 0
  if parts[1][1] == 'B'
    c += 100
  end
  if parts[1][2] == 'B'
    c += 10
  end
  if parts[1][3] == 'B'
    c += 1
  end
  rules[c] = parts[2][1] == 'B' ? 1 : 0
end

size = (2*n + 4)

fractal = fill(0, size)

fractal[n+2] = 1
  
for i in 1:n
  a, b, c = fractal[1], fractal[2], fractal[3]
  s = a * 100 + b * 10 + c
  for pos in 2:size-2
    fractal[pos] = rules[s]
    if (a == 1)
      s -= 100
    end
    a, b, c = b, c, fractal[pos+2]
    s *= 10
    s += c
  end
end

print(countnz(fractal))
