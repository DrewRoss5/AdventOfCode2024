# returns true if a list of reports is safe, otherwise false
def validate(arr: list[int]):
    safe = True
    increasing = (arr[1] > arr[0])
    print(f"{arr}\nIncreasing: {increasing}")
    for j in range(1, len(arr)):
        if increasing:
            dif = arr[j] - arr[j - 1]
        else:
            dif = arr[j - 1] - arr[j]
        if dif < 1 or dif > 3:
            safe = False
    return safe
        

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    # part 1
    count = 0
    for i in lines:
        arr = [i for i in map(lambda x: int(x), i.split(' '))]
        if validate(arr):
            count += 1
    print(f'Part 1: Count: {count}')


    
if __name__ == '__main__':
    main()