#!/usr/bin/docker run -i  --rm -v $PWD:/app -w /app julia julia solve.jl
expenses = Set()

for line in eachline()
    n = tryparse(Int, line)
    push!(expenses, n)
end

for n in expenses
    if (2020 - n) in expenses
        println("Two numbers ",n * (2020 - n))
        break
    end
    for n2 in expenses
        n3 = 2020 - n - n2
        if n3 in expenses
            println("Three numbers: ", n * n2 * n3)
            break
        end
    end
end
