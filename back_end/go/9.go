package main

import "fmt"

type person struct {
	name string
	age int
}

type dict struct {
	data map[int]string
}

func newDict() *dict {
	d := dict{}
	d.data = map[int]string{}
	return &d
}
func main() {
	p := person{}

	p.name = "lee"
	p.age = 10

	fmt.Println(p)

	var p1 = person{"bob", 20}
	p2 := person{name: "sean", age: 50}
	fmt.Println(p1, p2)

	p3 := new(person)
	p3.name = "lee"
	fmt.Println(p3)


	dic := newDict()
	dic.data[1] = "A"
	fmt.Println(dic)
}
