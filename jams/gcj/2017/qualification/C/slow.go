package main

import (
	"fmt"
	"container/heap"
	"math"
)

type Gap struct {
	index int
	size int
}

type GapHeap []*Gap

func (g GapHeap) Len() int           { return len(g) }
func (g GapHeap) Less(i, j int) bool {
	if g[i].size != g[j].size {
		return g[i].size > g[j].size
	} else {
		return g[i].index < g[j].index
	}
}
func (g GapHeap) Swap(i, j int)      { g[i], g[j] = g[j], g[i] }

func (g *GapHeap) Push(x interface{}) {
	*g = append(*g, x.(*Gap))
}

func (g *GapHeap) Pop() interface{} {
	old := *g
	n := len(old)
	x := old[n-1]
	*g = old[0 : n-1]
	return x
}

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

	gh := make(GapHeap, 0)
	heap.Init(&gh)

	initial_gap := &Gap{0, N}
	heap.Push(&gh, initial_gap)
	var last_gap Gap

	for i:=0; i < K; i++ {
		gap := heap.Pop(&gh).(*Gap)
		last_gap = *gap

		if gap.size == 2 {
			heap.Push(&gh, &Gap{gap.index + 1, gap.size - 1})
			max, min = 1, 0
		} else if gap.size > 2 {
			d := 1 - (gap.size % 2)
			first_gap_size := (gap.size / 2) - d
			heap.Push(&gh, &Gap{gap.index, first_gap_size})
			heap.Push(&gh, &Gap{gap.index + first_gap_size + 2, gap.size / 2})
			max, min = first_gap_size + d, first_gap_size
		} else {
			// Gap size 1
			max, min = 0, 0
		}
	}

	fmt.Println(N, K,last_gap)
	return fmt.Sprintf("%d %d", max, min)
}

func main() {
	var cases int
	fmt.Scanf("%d\n", &cases)

	for i := 1; i < cases + 1; i++ {
	    fmt.Printf("Case #%d: %s\n", i, Solve())
	}
}
