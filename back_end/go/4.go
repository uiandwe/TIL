package main

func main() {
	msg := "Hello"
	say(&msg)
	println(msg) //변경된 메시지 출력

	say1("This", "is", "a", "book")
	say1("Hi")

	total := sum(1, 7, 3, 5, 9)
	println(total)

	count, total := sum1(1, 7, 3, 5, 9)
	println(count, total)
}

func say(msg *string) {
	println(*msg)
	*msg = "Changed" //메시지 변경
}

func say1(msg ...string) {
	for _, s := range msg {
		println(s)
	}
}

func sum(nums ...int) int {
	s := 0
	for _, n := range nums {
		s += n
	}
	return s
}


func sum1(nums ...int) (int, int) {
	s := 0      // 합계
	count := 0  // 요소 갯수
	for _, n := range nums {
		s += n
		count++
	}
	return count, s
}