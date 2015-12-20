package main

import (
  "container/ring"
  "fmt"
  "runtime/pprof"
  "os"
)

func main() {
  var n, m int

  f, _ := os.Create("yes.pprof")
  pprof.StartCPUProfile(f)
  defer pprof.StopCPUProfile()

  fmt.Scan(&n)
  fmt.Scan(&m)

  bucket2number := make(map[int] *ring.Ring)
  number2bucket := map[int] int {0: 0, n-1: n-1}
  bucketlen := map[int] int {0:1, n-1: 1}

  bucket2number[0] = ring.New(1)
  bucket2number[0].Value = 0
  bucket2number[n-1] = ring.New(1)
  bucket2number[n-1].Value = n-1

  var a, b int
  var la, lb *ring.Ring
  var debug = false

  for i:= 0; i<=m; i++ {
    fmt.Scan(&a, &b)

    ba, ok := number2bucket[a]
    if ! ok {
      number2bucket[a] = a
      bucketlen[a] = 1
      ba = a
      la = ring.New(1)
      la.Value = a
      bucket2number[ba] = la
    } else {
      la = bucket2number[ba]
    }

    bb, ok := number2bucket[b]
    if ! ok {
      number2bucket[b] = b
      bucketlen[b] = 1
      bb = b
      lb = ring.New(1)
      lb.Value = b
      bucket2number[bb] = lb
    } else {
      lb = bucket2number[bb]
    }

    if ba != bb {
      // Not connected yet
      if bucketlen[ba] < bucketlen[bb] {
        la, lb = lb, la
        ba, bb = bb, ba
      }

      for j := 0; j < bucketlen[bb]; j++ {
        number2bucket[lb.Value.(int)] = ba
        lb = lb.Next()
      }

      la.Link(lb)
      bucketlen[ba] += bucketlen[bb]

      delete(bucket2number, bb)

      if number2bucket[0] == number2bucket[n-1] {
         fmt.Printf("Connected at %d\n", i)
         return
      }
    }

    if debug {
      fmt.Printf("%d -> %d\n", a, b)

      fmt.Print("Bucket2Number\n")
      for k, v := range bucket2number {
        fmt.Print(k)
        v.Do(
          func(x interface{}) {
            fmt.Printf(" %d", x.(int))
        })
        fmt.Println()
      }

      fmt.Print("Number2Bucket\n")
      for k, v := range number2bucket {
        fmt.Printf("%d: %d\n", k, v)
      }
    }
  }

  fmt.Println("Not connected")
}
