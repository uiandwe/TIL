package main

import (
	"fmt"
	"time"
)

func main() {
	go fun1()
	for i := 0; i < 20; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println("main", i)
	}
	fmt.Scanln()
}

func fun1() {
	for i := 0; i < 10; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println("fun1:", i)
	}
}