package main

func nextValue() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {
	next := nextValue()

	println(next())  // 1
	println(next())  // 2
	println(next())  // 3

	anotherNext := nextValue()
	println(anotherNext()) // 1 다시 시작
	println(anotherNext()) // 2


	var a [3]int  //정수형 3개 요소를 갖는 배열 a 선언
	a[0] = 1
	a[1] = 2
	a[2] = 3
	println(a[1]) // 2 출력

	var a1 = [3]int{1, 2, 3}
	var a3 = [...]int{1, 2, 3}


	var a2 = [2][3]int{
		{1, 2, 3},
		{4, 5, 6},  //끝에 콤마 추가
	}

}
