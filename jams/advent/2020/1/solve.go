package main

import (
	"fmt"
    "sort"
)

func main() {
    var i,n int

    expenses := make([]int, 0)
    for n = 1 ; n > 0; {
        n, _ = fmt.Scanf("%d\n", &i)
        if n > 0 && i <= 2020 {
            expenses = append(expenses, i)
        }
    }

    sort.Ints(expenses)

    for i = 0; i < len(expenses) ; i++ {
        for j := len(expenses) - 1; j > i ; j-- {
            if expenses[i] + expenses[j] == 2020 {
                fmt.Printf("%d\n", expenses[i] * expenses[j])
            }
        }
    }

    for i = 0; i < len(expenses) ; i++ {
        for j := 0; j < len(expenses) ; j++ {
            for k := 0; k < len(expenses) ; k++ {
                if expenses[i] + expenses[j] + expenses[k] == 2020 {
                    fmt.Printf("%d\n", expenses[i] * expenses[j] * expenses[k])
                }
            }
        }
    }
}
