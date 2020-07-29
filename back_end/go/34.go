package main

import (
	"fmt"
	"runtime/debug"
)


func r(){
	if r := recover(); r != nil {
		fmt.Println("recoverd", r)
		debug.PrintStack()
	}
}
func test() {
	defer r()
	arr := []int{5, 3, 7}

	fmt.Println(arr[3])
	fmt.Println("from test")

}
func main() {
	test()
	fmt.Println("exit")
}