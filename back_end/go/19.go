package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"os"
)

func main() {
	// 파일 생성
	file, err := os.Create("./output.csv")
	if err != nil {
		panic(err)
	}

	// csv writer 생성
	wr := csv.NewWriter(bufio.NewWriter(file))

	// csv 내용 쓰기
	wr.Write([]string{"A", "0.25"})
	wr.Write([]string{"B", "55.70"})
	wr.Flush()

	// 파일 오픈
	file1, _ := os.Open("./output.csv")

	// csv reader 생성
	rdr := csv.NewReader(bufio.NewReader(file1))

	// csv 내용 모두 읽기
	rows, _ := rdr.ReadAll()

	// 행,열 읽기
	for i, row := range rows {
		for j := range row {
			fmt.Printf("%s ", rows[i][j])
		}
		fmt.Println()
	}
}
