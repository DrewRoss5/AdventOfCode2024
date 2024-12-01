import sys

def main():
    left = []
    right = []
    with open("input") as f:
        lines = f.read().split("\n")[:-1]
    for i in lines:
        tmp = i.split("  ")
        left.append(int(tmp[0]))
        right.append(int(tmp[1]))
    # part one
    left.sort()
    right.sort()
    answer = 0
    for i in range(1000):
        answer += abs(left[i] - right[i])
    print(f"Part one: {answer}")
    # part two
    answer = 0
    for i in range(1000):
        tmp = left[i]
        answer += tmp * right.count(tmp)
    print(f"Part two: {answer}")


if __name__ == "__main__":
    main()