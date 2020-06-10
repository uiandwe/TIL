package main

import "fmt"

func check(val int) {
	switch val {
	case 1:
		fmt.Println("1 이하")
		fallthrough
	case 2:
		fmt.Println("2 이하")
		fallthrough
	case 3:
		fmt.Println("3 이하")
		fallthrough
	default:
		fmt.Println("default 도달")
	}
}

func main() {
	var a int = 10
	var f float32 = 11.
	print(a)
	print(f)

	var i, j, k int = 1, 2, 3
	print(i, j, k)

	const c int = 10
	const s string = "HI"
	println(c, s)
	var max = 10
	if val := i * 2; val < max {
		println(val)
	}


	var name string
	var category = 1

	switch category {
	case 1:
		name = "Paper Book"
	case 2:
		name = "eBook"
	case 3, 4:
		name = "Blog"
	default:
		name = "Other"
	}
	println(name)

	check(2)

}
