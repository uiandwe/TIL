package main

import (
	"fmt"
	"time"
)

func main() {
	// 시작 시간
	startTime := time.Now()

	// Task 실행
	for i := 0; i < 1000; i++ {
		println("Hello")
	}

	// 경과 시간
	elapsedTime := time.Since(startTime)

	fmt.Printf("실행시간: %s\n", elapsedTime)
}
