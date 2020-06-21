package main

import "fmt"

type Address struct {
	street string
}

type Person struct {
	name string
	age int
	address Address
}


func main() {
	p := Person{}
	p.name = "test"
	p.age = 10
	p.address.street = "??"
	fmt.Println(p)
}
