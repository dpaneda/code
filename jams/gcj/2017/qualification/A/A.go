package main

import "fmt"
import "strconv"

func Flip(pancakes []rune, n, K int) {
	for i := n; i < n + K; i++ {
		if pancakes[i] == '-' {
			pancakes[i] = '+'
		} else {
			pancakes[i] = '-'
		}
	}
}

func Solve() string {
	var s string
	var K int

	fmt.Scanf("%s %d\n", &s, &K)
	pancakes := []rune(s)

	flips := 0

	for i:= 0; i < len(pancakes); i++ {
		if i + K > len(pancakes) && pancakes[i] == '-' {
			return "IMPOSSIBLE"
		}

		if pancakes[i] == '-' {
			flips += 1
			Flip(pancakes, i, K)
		}
	}

	return strconv.Itoa(flips)
}

func main() {
	var cases int
	fmt.Scanf("%d\n", &cases)

	for i := 1; i < cases + 1; i++ {
	    fmt.Printf("Case #%d: %s\n", i, Solve())
	}
}
