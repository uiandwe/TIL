package main

import (
	"encoding/json"
	"fmt"
)

type Member struct {
	Name string
	Age int
	Active bool
}
func main() {
	mem := Member{"Alex", 10, true}

	jsonBytes, err := json.Marshal(mem)
	if err != nil {
		panic(err)
	}

	jsonString := string(jsonBytes)
	fmt.Println(jsonString)

	var mem1 Member
	err1 := json.Unmarshal(jsonBytes, &mem1)
	if err1 != nil {
		panic(err1)
	}

	fmt.Println(mem1.Name, mem1.Age, mem1.Active)
}
