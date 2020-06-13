package main

import (
	"io"
	"os"
)

func main() {
	fi, err := os.Open("./1.txt")
	if err != nil {
		panic(err)
	}
	defer fi.Close()

	// 출력파일 생성

	fo, err := os.Create("2.txt")
	if err != nil {
		panic(err)
	}
	defer fo.Close()

	buff := make([]byte, 1024)

	// 루프
	for {
		// 읽기
		cnt, err := fi.Read(buff)
		if err != nil && err != io.EOF {
			panic(err)
		}

		// 끝이면 루프 종료
		if cnt == 0 {
			break
		}

		// 쓰기
		_, err = fo.Write(buff[:cnt])
		if err != nil {
			panic(err)
		}
	}
}
