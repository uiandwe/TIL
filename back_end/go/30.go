package main
 
import (
    "fmt"
    "net/http"
)
 
func main() {
    // "/" 경로로 접속했을 때 처리할 핸들러 함수 지정
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        // "welcome!" 문자열을 화면에 출력
        fmt.Fprintln(w, "welcome!")
    })

    http.HandleFunc("/about", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "about")
    })
 

    // 8080 포트로 웹 서버 구동
    http.ListenAndServe(":8080", nil)
}
