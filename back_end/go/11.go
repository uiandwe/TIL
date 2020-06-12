package main

import "math"
import "fmt"

type Shape interface{
	area() float64
	perimeter() float64
}

type Rect struct {
	width, height float64
}

//Circle 정의
type Circle struct {
	radius float64
}

//Rect 타입에 대한 Shape 인터페이스 구현
func (r Rect) area() float64 { return r.width * r.height }
func (r Rect) perimeter() float64 {
	return 2 * (r.width + r.height)
}

//Circle 타입에 대한 Shape 인터페이스 구현
func (c Circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c Circle) perimeter() float64 {
	return 2 * math.Pi * c.radius
}

func main() {
		r := Rect{10, 20}
		c := Circle{10}
		showArea(r, c)

		var x interface{}
		x = 1
		x = "tom"
		fmt.Println(x)

		var a interface{} = 1
		i := a
		j := a.(int)
		fmt.Println(&i)
		fmt.Println(j)
}

func showArea(shapes ...Shape) {
	for _, s := range shapes {
		a := s.area() //인터페이스 메서드 호출
		fmt.Println(a)
	}
}
