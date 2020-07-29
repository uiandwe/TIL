package main

import (
	"fmt"
	"sync"
)

func Min(a []int) int{
	if len(a) == 0{
		return 0
	}
	min := a[0]
	for _, e := range a[1:] {
		if min > e{
			min = e
		}
	}
	return min
}

func ParalleMin(a []int, n int) int{
	if len(a) < n {
		return Min(a)
	}
	mins := make([]int, n)
	size := (len(a) + n-1) /n
	var wg sync.WaitGroup
	for i:=0; i<n; i++{
		wg.Add(1)
		go func(i int){
			defer wg.Done()
			begin, end := i*size, (i+1)*size
			if end > len(a){
				end = len(a)
			}
			mins[i] = Min(a[begin:end])
		}(i)
	}
	wg.Wait()
	return Min(mins)

}

func main() {
	fmt.Println(ParalleMin([]int {10, 9, 5, 4, 8, 3, 5, 6, 7, 234, 346, 68, 57, 2345, 23, 1}, 4))
}
