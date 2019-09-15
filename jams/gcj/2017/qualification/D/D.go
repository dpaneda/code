package main

import (
	"fmt"
)

func PrintGrid(grid [][]rune){
	for _, line := range grid {
		fmt.Println(string(line))
	}
}

type Change struct {
	what rune
	x, y int
}

func Solve() string {
	var N,M int

	fmt.Scanf("%d %d\n", &N, &M)
	var (
		c rune
		x,y int
	)
	grid := make([][]rune, N)
	for i:=0; i < N; i++ {
		grid[i] = make([]rune, N)
		for j:=0; j < N; j++ {
			grid[i][j] = '.'
		}
	}

	row_map := make(map[int]int)
	diag_map := make(map[int]int)
	diag2_map := make(map[int]int)

	for i:=0; i < M; i++ {
		fmt.Scanf("%c %d %d\n", &c, &x, &y)
		x, y = x - 1, y - 1
		grid[x][y] = c

		if c != '+' {
			row_map[x] += 1
		}

		if c != 'x' {
			diag_map[x+y] += 1
			diag2_map[x-y] += 1
		}
	}

	PrintGrid(grid)

	changes := 0
	s := ""

	for i:=0; i < N; i++ {
		for j:=0; j < N; j++ {
			d := 0
			switch {
			case grid[i][j] == '+':
				d += 2
			case grid[i][j] == 'x':
				d += 1
			}

			if (row_map[i] + diag_map[i+j] + diag2_map[i-j]) == d {
				row_map[i] += 1
				diag_map[i+j] += 1
				diag2_map[i-j] += 1
				s+= fmt.Sprintf("%c %d %d\n", 'o', i, j)
				grid[i][j] = 'o'
				changes += 1
			}
		}
	}

	for i:=0; i < N; i++ {
		for j:=0; j < N; j++ {
			if row_map[i] == 0 {
				row_map[i] += 1
				grid[i][j] = 'x'
				s += fmt.Sprintf("%c %d %d\n", 'x', i, j)
				changes += 1
			}
		}
	}

	for i:=0; i < N; i++ {
		for j:=0; j < N; j++ {
			if (diag_map[i+j] + diag2_map[i-j]) == 0 {
				diag_map[i+j] += 1
				diag2_map[i+j] += 1
				s += fmt.Sprintf("%c %d %d\n", '+', i, j)
				grid[i][j] = '+'
				changes += 1
			}
		}
	}

	points := 0
	for i:=0; i < N; i++ {
		for j:=0; j < N; j++ {
			if (grid[i][j] == 'o') {
				points += 2
			} else if grid[i][j] != '.' {
				points += 1
			}
		}
	}

	PrintGrid(grid)

	s = fmt.Sprintf("%d %d\n", points, changes) + s
	return s
}

func main() {
	var cases int
	fmt.Scanf("%d\n", &cases)

	for i := 1; i < cases + 1; i++ {
	    fmt.Printf("Case #%d: %s", i, Solve())
	}
}
