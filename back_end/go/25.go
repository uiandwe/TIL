package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Result struct {
	strike int
	ball int
}

func main() {
	numbers := MakeNumbers()

	fmt.Println(numbers)

	cnt := 0
	for {
		cnt++
		inputNumbers := InputNumbers()

		result := CompareNumbers(numbers, inputNumbers)

		PrintResult(result)

		if IsGameEnd(result) {
			break
		}
	}
	fmt.Printf("%d\n", cnt)

}


func MakeNumbers() [3]int {
	var rst [3]int
	a := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(a), func(i, j int) { a[i], a[j] = a[j], a[i] })

	for i:=0; i<3; i++{
		rst[i] = a[i]
	}
	return rst
}

func InputNumbers() [3]int {
	var rst [3]int
	for {
		var no int
		_, err := fmt.Scanf("%d", &no)
		if err != nil {
			fmt.Println("fuck input")
			continue
		}

		idx := 2
		for no > 0 {
			n := no%10
			no = no/10
			rst[idx] = n
			idx--
		}
		break
	}

	return rst
}

func CompareNumbers(numbers [3]int, inputNumbers [3]int) Result{

	strike := 0
	balls := 0

	for i:=0; i< 3; i++{
		for j:=0; j<3; j++{
			if numbers[i] == inputNumbers[j]{
				if i == j{
					strike++
				} else{
					balls++
				}
				break
			}
		}
	}
	return Result{strike, balls}
}

func PrintResult(result Result){
	fmt.Printf("%dS%dB\n", result.strike, result.ball)
}

func IsGameEnd(result Result) bool{
	if result.strike == 3 {
		return true
	}

	return false
}