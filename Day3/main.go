package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	// read the file
	fileBytes, err := os.ReadFile("input.txt")
	input := string(fileBytes)
	if err != nil {
		return
	}
	re := regexp.MustCompile("mul\\([0-9]+,[0-9]+\\)")
	commands := re.FindAllString(input, -1)
	var lhs, rhs int
	var operands []string
	sum := 0
	for i := 0; i < len(commands); i++ {
		operands = strings.Split(commands[i][4:len(commands[i])-1], ",")
		lhs, _ = strconv.Atoi(operands[0])
		rhs, _ = strconv.Atoi(operands[1])
		sum += lhs * rhs
	}
	fmt.Printf("Sum: %v\n", sum)
}
