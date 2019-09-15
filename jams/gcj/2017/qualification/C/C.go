package main

import (
	"fmt"
	"math"
)

func Solve() string {
	var N,K,max,min,gap_size,leafs,tree_nodes,used_leafs,min_value,higher_leafs int

	fmt.Scanf("%d %d\n", &N, &K)
	// Level of the last gap
	level := uint(math.Ceil(math.Log2(float64(K + 1))))
	fmt.Printf("Level of the last gap: %d\n", level)
	// Check number of used leafs on the last level
	if (level > 1) {
		leafs = 2 << (level - 2)
		tree_nodes = leafs - 1
		used_leafs = K - tree_nodes
		fmt.Printf("Leafs %d Nodes %d Used %d\n", leafs, tree_nodes, used_leafs)

		// Calculate the value of the gaps on the last level
		min_value = (N - tree_nodes) / leafs
		higher_leafs = (N - tree_nodes) % leafs
		fmt.Printf("Leaf value %d Higher values %d\n", min_value, higher_leafs)
		// Time to check which gap we got
		gap_size = min_value
		if used_leafs <= higher_leafs {
			// High gap
			gap_size += 1
		}

		if gap_size == 1 {
			max, min = 0, 0
		} else {
			max = gap_size / 2
			min = max
			if (gap_size % 2) == 0 {
				min -= 1
			}
		}
	} else {
		max = N / 2
		min = max -  ((N - 1) % 2)
	}

	fmt.Printf("Gap size %d\n", gap_size)
	return fmt.Sprintf("%d %d", max, min)
}

func main() {
	var cases int
	fmt.Scanf("%d\n", &cases)

	for i := 1; i < cases + 1; i++ {
	    fmt.Printf("Case #%d: %s\n", i, Solve())
	}
}
