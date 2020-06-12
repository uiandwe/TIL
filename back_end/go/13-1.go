package main

func main() {
	// 정수형 채널을 생성한다
	ch := make(chan int)

	go func() {
		ch <- 123   //채널에 123을 보낸다
	}()

	var i int
	i = <- ch  // 채널로부터 123을 받는다
	println(i)
}