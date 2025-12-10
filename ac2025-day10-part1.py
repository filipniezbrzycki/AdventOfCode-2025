import re
from collections import deque

def parseLine(line: str):
    before_brace = line.split('{', 1)[0].strip()
    m = re.search(r'\[([.#]+)\]', before_brace)
    pattern = m.group(1)
    n = len(pattern)
    target_mask = 0
    for i, ch in enumerate(pattern):
        if ch == '#':
            target_mask |= (1 << i)
        else:
            continue
    button_specs = re.findall(r'\(([^)]*)\)', before_brace)
    button_masks = []
    for spec in button_specs:
        spec = spec.strip()
        if not spec:
            continue
        indices = [s.strip() for s in spec.split(',') if s.strip() != ""]
        mask = 0
        for idx_str in indices:
            idx = int(idx_str)
            mask |= (1 << idx)
        button_masks.append(mask)
    return target_mask, button_masks, n

def minPresses(target_mask: int, button_masks, n: int) -> int:
    num_states = 1 << n
    dist = [-1] * num_states
    start = 0
    dist[start] = 0
    q = deque([start])
    while q:
        state = q.popleft()
        d = dist[state]
        for bm in button_masks:
            next_state = state ^ bm
            if dist[next_state] == -1:
                dist[next_state] = d + 1
                if next_state == target_mask:
                    return dist[next_state]
                q.append(next_state)

totalPresses = 0
with open("data-2025-day10.txt", "r") as f:
    for line in f:
        parsed = parseLine(line.strip())
        targetMask, buttonMask, n = parsed
        presses = minPresses(targetMask, buttonMask, n)
        totalPresses += presses

print(totalPresses)
