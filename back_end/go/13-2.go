package main

import "fmt"

func main() {
	ch := make(chan string, 1)
	sendChan(ch)
	receiveChan(ch)

	close(ch)

	// 채널 수신
	println(<-ch)
	println(<-ch)

	if _, success := <-ch; !success {
		println("더이상 데이타 없음.")
	}
	for i := range ch {
		println(i)
	}
}

func sendChan(ch chan<- string) {
	ch <- "Data"
	// x := <-ch // 에러발생
}

func receiveChan(ch <-chan string) {
	data := <-ch
	fmt.Println(data)
}