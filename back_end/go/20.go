package main

import (
	"container/list"
	"fmt"
)

func main() {
	//새 이중 연결 리스트 생성
	mylist := list.New()

	// 리스트 요소 추가
	mylist.PushBack("A")
	mylist.PushBack(100)
	mylist.PushBack(true)
	mylist.PushFront("A")

	// 리스트 Iteration
	for e := mylist.Front(); e != nil; e = e.Next() {
		fmt.Println(e.Value)
	}
}
