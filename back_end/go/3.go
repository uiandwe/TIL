package main

func main() {
	sum := 0
	for i :=1; i<= 100; i++ {
		sum += i
	}
	println(sum)

	n := 1
	for n < 100 {
		n *= 2
	}
	println(n)

	names := []string{"홍길동", "이순신", "강감찬"}

	for index, name := range names {
		println(index, name)
	}

	var a = 1
	for a < 15 {
		if a == 5 {
			a += a
			continue // for루프 시작으로
		}
		a++
		if a > 10 {
			break  //루프 빠져나옴
		}
	}
	if a == 11 {
		goto END //goto 사용예
	}
	println(a)

END:
	println("End")

	i := 0
L1:
	for {

		if i == 0 {
			break L1
		}
	}

	println("OK")
}
