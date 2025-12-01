def turn(cur, trn):
    steps = int(trn[1:])
    if trn[0] == "L":
        if cur == 0:
            hits = steps // 100
        else:
            a = cur - steps
            if a > 0:
                hits = 0
            else:
                hits = 1 + ((-a) // 100)
        return hits, (cur - steps) % 100
    else:
        return (cur + steps) // 100, (cur + steps) % 100

pos = 50
passwd = 0
with open("data-2025-day1.txt", "r") as f:
    for line in f:
        cross, pos=turn(pos, line)
        passwd += cross
print(passwd)