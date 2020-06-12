package main

func calc(f func(int, int) int, a int, b int) int {
	result := f(a, b)
	return result
}

func main() {
	sum := func(n ...int) int{
		s := 0
		for _, i := range n{
			s += i
		}
		return s
	}
	result := sum(1, 2, 3, 4, 5)
	println(result)

	add := func(i int, j int) int {
		return i + j
	}

	// add 함수 전달
	r1 := calc(add, 10, 20)
	println(r1)

	// 직접 첫번째 파라미터에 익명함수를 정의함
	r2 := calc(func(x int, y int) int { return x - y }, 10, 20)
	println(r2)
}
