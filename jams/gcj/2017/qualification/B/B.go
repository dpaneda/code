package main

import "fmt"

func FixNumber(number []int, i int) string {
	// Walk to find fix point
	for ; i > 0 && number[i] <= number[i - 1]; i-- {
	}

	if i == 0 && number[i] <= 1 {
		// No point to fix, remove fist digit
		number = number[1:]
		number[0] = 9
	} else {
		number[i]--
	}

	tidy := make([]rune, 0)
	for j, n := range number {
		if j <= i {
			tidy = append(tidy, rune('0' + n))
		} else {
			tidy = append(tidy, '9')
		}
	}

	return string(tidy)
}

func Solve() string {
	var s string

	fmt.Scanf("%s\n", &s)
	number := make([]int, 0, len(s))
	for _, r := range s {
		i := int(r - '0')
        number = append(number, i)
    }

	last_digit := number[0]

	for i:= 1; i < len(number); i++ {
		if number[i] < last_digit {
			return FixNumber(number, i - 1)
		}

		last_digit = number[i]
	}

	return s
}

func main() {
	var cases int
	fmt.Scanf("%d\n", &cases)

	for i := 1; i < cases + 1; i++ {
	    fmt.Printf("Case #%d: %s\n", i, Solve())
	}
}
