package main
import "fmt"

func main() {
	var m = make(map[int]string)
	m[91] = "apple"
	m[123] = "grap"
	m[777] = "tomato"

	str := m[91]
	fmt.Println(str)

	no := m[1]
	fmt.Println(no)

	delete(m, 777)
	fmt.Println(m)

	tickers := map[string]string{
		"GOOG": "Google Inc",
		"MSFT": "Microsoft",
		"FB":   "FaceBook",
		"AMZN": "Amazon",
	}

	// map 키 체크
	val, exists := tickers["MSFT"]
	if !exists {
		println("No MSFT ticker")
	}
	println(val)

	myMap := map[string]string{
		"A": "Apple",
		"B": "Banana",
		"C": "Charlie",
	}

	// for range 문을 사용하여 모든 맵 요소 출력
	// Map은 unordered 이므로 순서는 무작위
	for key, val := range myMap {
		fmt.Println(key, val)
	}
}
