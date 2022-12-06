
def solve():
    N, K = list(map(int, input().split()))
    l = list(set(map(int, input().split())))
    l.sort()
    #print (N, K, l)

    def check_range(a, b):
        #print(f"Check range {a} - {b}")
        if a == None:
            pick = b - 1
            win_tickets = max(0, b - 1)
        elif b == None:
            pick = a + 1
            win_tickets = max(0, K - a)
        else:
            pick = a + 1
            win_tickets = (b - a) // 2
        return pick, win_tickets
       
    ranges = []
    ranges.append(check_range(None, l[0]))
    for i in range(len(l) - 1):
        ranges.append(check_range(l[i], l[i+1]))
    ranges.append(check_range(l[-1], None))
    #print(ranges)
    ranges.sort(key=lambda tup: tup[1])
    prob = (ranges[-1][1] / K) + (ranges[-2][1] / K)

    #Corner case, pick two in a same range to reserve the entire range
    longest_range = 0 
    for i in range(len(l) - 1):
        range_len = l[i+1] - l[i] - 1
        if range_len > longest_range:
            longest_range = range_len
    #print(longest_range)

    longest_range_prob = longest_range / K
    return max(prob, longest_range_prob)
     

cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
