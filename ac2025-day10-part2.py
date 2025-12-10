import re
from typing import List, Tuple
import pulp

def parseLine(line: str) -> Tuple[List[int], List[List[int]]]:
    m = re.search(r'\{([^}]*)\}', line)
    jolts_str = m.group(1)
    targets = [int(x.strip()) for x in jolts_str.split(',') if x.strip() != ""]
    before_brace = line.split('{', 1)[0]
    button_specs = re.findall(r'\(([^)]*)\)', before_brace)
    buttons: List[List[int]] = []
    for spec in button_specs:
        spec = spec.strip()
        if not spec:
            buttons.append([])
            continue
        idxs = [int(s.strip()) for s in spec.split(',') if s.strip() != ""]
        buttons.append(idxs)
    return targets, buttons

def minPresses(targets: List[int], buttons: List[List[int]]) -> int:
    m = len(targets)
    k = len(buttons)
    touched = [False] * m
    for _, S in enumerate(buttons):
        for i in S:
            touched[i] = True
    if m == 0:
        return 0
    prob = pulp.LpProblem("JoltageConfig", pulp.LpMinimize)
    x = [
        pulp.LpVariable(f"x_{j}", lowBound=0, cat=pulp.LpInteger)
        for j in range(k)
    ]
    prob += pulp.lpSum(x), "TotalButtonPresses"
    for i in range(m):
        prob += (
            pulp.lpSum(x[j] for j in range(k) if i in buttons[j]) == targets[i],
            f"counter_{i}"
        )
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[prob.status] != "Optimal":
        raise RuntimeError(f"ILP could not find optimal solution, status: {pulp.LpStatus[prob.status]}")
    result = int(round(pulp.value(pulp.lpSum(x))))
    return result

totalPresses = 0
with open("data-2025-day10.txt", "r") as f:
    for line in f:
        parsed = parseLine(line.strip())
        targets, buttons = parsed
        presses = minPresses(targets, buttons)
        totalPresses += presses

print(totalPresses)
