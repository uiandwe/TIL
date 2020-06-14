package main

import (
	"os"
	"strconv"
	"time"
)

/* 비동기 로깅 */
var logChannel chan string
func logSetup(logFile string) {

	// 로그 파일이 없으면, 생성한다
	if _, err := os.Stat(logFile); os.IsNotExist(err) {
		f, _ := os.Create(logFile)
		f.Close()
	}

	// 로그 채널을 만든다
	logChannel = make(chan string, 100)

	// 채널을 통한 비동기 로깅
	go func() {
		// 채널이 닫힐 때까지 메시지 받으면 로깅
		for msg := range logChannel {
			f, _ := os.OpenFile(logFile, os.O_APPEND, os.ModeAppend)
			f.WriteString(time.Now().String() + " " + msg + "\n")
			f.Close()
		}
	}()
}

/* 테스트 코드 */
func main() {
	logSetup("./logfile.txt")

	go func() {
		for i := 1; i < 20; i++ {
			n := strconv.Itoa(i)
			println(n)
			logChannel <- n
		}
	}()

	go func() {
		for i := 100; i < 120; i++ {
			logChannel <- strconv.Itoa(i)
		}
	}()

	time.Sleep(1 * time.Second)
	close(logChannel)
}