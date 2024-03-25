
from collections import Counter

def solution(weights):
    counter = Counter(weights)

    sameCount = 0
    count = 0

    for v in counter.values():
        if v > 1:
            sameCount += (v*(v-1)) // 2

    for weight in weights:
        # Check for targets
        targets = []

        if weight * 3 // 2 == weight * 3 / 2:
            targets.append(weight * 3 // 2)
        if weight * 4 // 3 == weight * 4 // 3:
            targets.append(weight * 4 // 3)
        targets.append(weight * 2)

        for target in targets:
            if target != weight and target in counter:
                count += counter[target]
    return count + sameCount