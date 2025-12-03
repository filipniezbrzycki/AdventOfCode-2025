with open("data-2025-day3.txt", "r") as f:
    joltage = 0
    for line in f:
        joltage_string = ""
        bank = list(line.strip())
        count = -11
        pos = 0
        while count <= 0:
            if count == 0:
                biggest = max(bank[pos:])
            else:
                biggest = max(bank[pos:count])
            where_biggest = list(filter(lambda i: bank[i] == biggest, range(pos, len(bank) + count)))
            joltage_string += bank[where_biggest[0]]
            count += 1
            pos=where_biggest[0]+1
        joltage += int(joltage_string)
print(joltage)