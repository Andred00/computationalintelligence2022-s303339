import random
import numpy

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

def goal_test(state, N):
    goal = set(range(N))
    covered = set()
    for l in state:
        for num in l:
            covered.add(num)
            if covered == goal:
                return True
    return False

print(problem(4, 42))