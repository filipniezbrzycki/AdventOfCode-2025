with open("data-2025-day2.txt", "r") as f:
    sumIDs = 0
    for rangeStr in f.read().split(','):
        start, end = map(int, rangeStr.split('-'))
        for num in range(start, end + 1):
            num_str = str(num)
            if len(str(num)) % 2 == 0:
                if num_str[:len(str(num)) // 2] == num_str[len(str(num)) // 2:]:
                    sumIDs += num
print(sumIDs)