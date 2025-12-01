def turn(cur, tr):
    steps = int(tr[1:])
    if tr[0] == "L":
        return (cur - steps) % 100
    else:
        return (cur + steps) % 100

pos = 50
passwd = 0
with open("data-2025-day1.txt", "r") as f:
    for line in f:
        pos=turn(pos, line)
        if pos == 0:
            passwd += 1
print(passwd)