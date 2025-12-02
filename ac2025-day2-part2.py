with open("data-2025-day2.txt", "r") as f:
    sumIDs = 0
    for rangeStr in f.read().split(','):
        start, end = map(int, rangeStr.split('-'))
        for num in range(start, end + 1):
            num_str = str(num)
            if len(str(num)) > 1:
                for pat_len in range(1, len(str(num)) // 2 + 1 ):
                    if len(str(num)) % pat_len == 0:
                        pattern = num_str[:pat_len]
                        repeats = len(str(num)) // pat_len
                        if pattern * repeats == num_str:
                            sumIDs += num
                            break
print(sumIDs)