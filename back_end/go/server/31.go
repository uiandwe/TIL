//Go - net/http 미들웨어 - Log 사용 예제
package main

import (
	"fmt"
	"log"
	"net/http"
)

//미들웨어 함수 선언(Return : func)
func logging(f http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println("MiddleWare Test(Log) : ", r.URL.Path)
		f(w, r)
	}
}

//요청1 핸들러
func req_test1(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Requested : (/req-test1)")
}

//요청2 핸들러
func req_test2(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Requested : (/req-test2)")
}

func main() {

	//핸들러 메소드 지정1
	http.HandleFunc("/req-test1", logging(req_test1))
	//핸들러 메소드 지정2
	http.HandleFunc("/req-test2", logging(req_test2))

	//기본 출력
	fmt.Println("Golang WebServer Working!")

	//서버 시작
	http.ListenAndServe(":9090", nil)

}
