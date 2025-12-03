with open("data-2025-day3.txt", "r") as f:
    joltage = 0
    for line in f:
        bank = list(line.strip())
        biggest = max(bank)
        where_biggest = list(filter(lambda i: bank[i] == biggest, range(len(bank))))
        if len(where_biggest) > 1:
            joltage += int(f'{biggest}{biggest}')
        else:
            if where_biggest[0] == len(bank)-1:
                second_biggest = max(bank[:-1])
                joltage += int(f'{second_biggest}{biggest}')
            else:
                second_biggest = max(bank[where_biggest[0]+1:])
                joltage += int(f'{biggest}{second_biggest}')
print(joltage)