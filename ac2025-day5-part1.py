ranges = []
fresh = 0
with open("data-2025-day5.txt", "r") as f:
    ranges_in_file = True
    for line in f:
        line = line.strip()
        if ranges_in_file:
            if line == "":
                ranges_in_file = False
                continue
            rng = line.strip().split("-")
            ranges.append(rng)
        else:
            for rng in ranges:
                if int(rng[0]) <= int(line) <= int(rng[1])+1:
                    fresh += 1
                    break
print(fresh)