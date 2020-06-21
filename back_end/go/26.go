package main

import "fmt"

func main() {
	greeter := gophersGreeter{"Hello", "gophers"}
	greeter.greet("Hello", "gophers")
}

type gophersGreeter struct {
	how string
	who string
}

func (greeter gophersGreeter) greet(how string, who string) {
	fmt.Printf("%s %s!", greeter.how, greeter.who)
}
