package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	// name := "Go Developers"
	current_time := time.Now()
	var first_num int = 0
	var second_num int = 0
	var math_operation string = ""
	fmt.Println("Azure for", first_num, second_num)
	f, err := os.OpenFile("history_calculator.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		panic(err)
	}
	for true {
		fmt.Println("\nEnter first num: ")
		fmt.Scan(&first_num)
		fmt.Println("Enter second num: ")
		fmt.Scan(&second_num)
		fmt.Printf("Enter a math operation between %d and %d: ", first_num, second_num)
		fmt.Scan(&math_operation)
		var result_operation int = 0
		current_date := fmt.Sprintf("%d %s %d", current_time.Day(), current_time.Month().String(), current_time.Year())
		fmt.Println(current_date)
		if math_operation == "+" {
			result_operation = first_num + second_num
			fmt.Printf("Result is: %d %s %d = %d", first_num, math_operation, second_num, result_operation)
		} else if math_operation == "-" {
			result_operation = first_num - second_num
			fmt.Printf("Result is: %d %s %d = %d", first_num, math_operation, second_num, result_operation)
		} else if math_operation == "*" {
			result_operation = first_num * second_num
			fmt.Printf("Result is: %d %s %d = %d", first_num, math_operation, second_num, result_operation)
		} else if math_operation == "/" {
			if second_num > 0 {
				result_operation = first_num / second_num
				fmt.Printf("Result is: %d %s %d = %d", first_num, math_operation, second_num, result_operation)
			} else {
				fmt.Printf("This operation doesn't exist")
			}
		} else if math_operation == "%" && second_num > 0 {
			if second_num > 0 {
				result_operation = first_num % second_num
				fmt.Printf("Result is: %d %s %d = %d", first_num, math_operation, second_num, result_operation)
			} else {
				fmt.Printf("This operation doesn't exist")
			}
		} else if math_operation == "exit" || math_operation == "EXIT" || math_operation == "Exit" {
			break
		}
		res := fmt.Sprintf("Result: %d %s %d = %d ; Date: %s \n", first_num, math_operation, second_num, result_operation, current_date)
		f.WriteString(res)
	}
}
