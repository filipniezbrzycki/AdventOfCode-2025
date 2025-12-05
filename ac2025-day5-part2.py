ranges = []
ingridients = 0
with open("data-2025-day5.txt", "r") as f:
    ranges_in_file = True
    for line in f:
        line = line.strip()
        if ranges_in_file:
            if line == "":
                ranges_in_file = False
                continue
            rng = line.strip().split("-")
            ranges.append([int(rng[0]), int(rng[1])])
        else:
            break
ranges.sort(key=lambda x: x[0])
cur_start, cur_end = ranges[0]
for start,end in ranges[1:]:
    if start <= cur_end:
        if end > cur_end:
            cur_end = end
    else:
        ingridients += (cur_end - cur_start +1)
        cur_start, cur_end = start, end
ingridients += (cur_end - cur_start +1)
print(ingridients)