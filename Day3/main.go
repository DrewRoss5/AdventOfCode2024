package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func ParseMul(mulStr string) int {
	operands := strings.Split(mulStr[4:len(mulStr)-1], ",")
	lhs, _ := strconv.Atoi(operands[0])
	rhs, _ := strconv.Atoi(operands[1])
	return lhs * rhs
}

func main() {
	// read the file
	fileBytes, err := os.ReadFile("input.txt")
	input := string(fileBytes)
	if err != nil {
		return
	}
	// part 1
	re := regexp.MustCompile("mul\\([0-9]+,[0-9]+\\)")
	commands := re.FindAllString(input, -1)
	sum := 0
	for i := 0; i < len(commands); i++ {
		sum += ParseMul(commands[i])
	}
	fmt.Printf("Part one sum: %v\n", sum)
	// part 2
	re = regexp.MustCompile("(mul\\([0-9]+,[0-9]+\\))|do(n't)?\\(\\)")
	commands = re.FindAllString(input, -1)
	sum = 0
	active := true
	for i := 0; i < len(commands); i++ {
		switch strings.Split(commands[i], "(")[0] {
		case "mul":
			if active {
				sum += ParseMul(commands[i])
			}
		case "do":
			active = true
		case "don't":
			active = false

		}
	}
	fmt.Printf("Part two sum: %v\n", sum)
}
