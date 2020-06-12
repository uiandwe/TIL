package main
import "fmt"

type Rect struct {
	width, height int
}

func (r Rect) area() int{
	return r.width * r.height
}

func (r *Rect) area2() int {
	r.width++
	return r.width * r.height
}

func main() {
	rect := Rect{10, 10}
	area := rect.area()
	fmt.Println(area)

	rect2 := Rect{10, 10}
	area2 := rect2.area2()
	fmt.Println(area2)
}
