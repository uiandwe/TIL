package main
import "fmt"


func main() {
	var a = []int{1, 2, 3}
	a[1] = 10
	fmt.Println(a)

	s := make([]int, 5, 10)
	fmt.Println(len(s), cap(s))

	var s1 []int
	if s1 == nil {
		fmt.Println("nil")
	}
	fmt.Println(len(s1), cap(s1))

	s2 := []int{0, 1, 2, 3, 4, 5}
	temp1 := s2[2:5]
	fmt.Println(temp1)

	temp2 := s2[1:]
	fmt.Println(temp2)

	s2 = append(s2, 6, 7, 8, 9)
	fmt.Println(s2)

	sliceA := make([]int, 0, 3)
	for i:= 1; i <= 15; i++ {
		sliceA = append(sliceA, i)
		fmt.Println(len(sliceA), cap(sliceA))
	}
	fmt.Println(sliceA)

	source := []int{0, 1, 2}
	target := make([]int, len(source), cap(source)*2)
	copy(target, source)
	fmt.Println(target)
	fmt.Println(len(target), cap(target))
}
