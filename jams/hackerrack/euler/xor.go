package main

import "fmt"

func main() {
  ascii := make([]int, 1)
  var n int

  for {
    read, _ := fmt.Scan(&n)
    ascii = append(ascii, n)
    if read == 0 {
      break
    }
    fmt.Println("read number", n, "from stdin")
  }

  letters := string([]byte, len(ascii))

  for i, n := range ascii {
    letters[i] = n
    fmt.Println("read letter", letters[i], "from stdin")
  }
}
