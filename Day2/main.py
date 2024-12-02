# returns a list of indices that are unsafe
def validate(arr: list[int]) -> bool:
    safe = True
    increasing = (arr[1] > arr[0])
    safe = True
    for j in range(1, len(arr)):
        if increasing:
            dif = arr[j] - arr[j - 1]
        else:
            dif = arr[j - 1] - arr[j]
        if dif < 1 or dif > 3:
            safe = False
            break
    return safe
        

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    part_one_count = 0
    part_two_count = 0
    for i in lines:
        arr = [i for i in map(lambda x: int(x), i.split(' '))]
        # check if the array is valid without modification
        valid = validate(arr)
        if valid:
            part_one_count += 1
            part_two_count += 1
        # check if removing one element makes the array valid
        else:
            for j in range(len(arr)):
                val = arr[j]
                arr.pop(j)
                if validate(arr):
                    part_two_count += 1
                    break
                arr.insert(j, val)
                
    print(f'Part 1 count: {part_one_count}\nPart 2 count {part_two_count}')

    
if __name__ == '__main__':
    main()
