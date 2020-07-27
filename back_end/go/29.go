package main

import (
	"fmt"
	"reflect"
)
type Value struct {
	v int
}

func main() {
	var m map[string]string
	m = make(map[string]string)
	m["abc"] = "bbb"


	m["123"] = "123"
	for key, value := range m {
		fmt.Println("Key:", key, "Value:", value)
	}

	keys := reflect.ValueOf(m).MapKeys()
	fmt.Println(keys)
}
