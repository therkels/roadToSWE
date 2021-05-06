def triple_step_recurse(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return triple_step_recurse(n-1) + triple_step_recurse(n-2) + triple_step_recurse(n-3)

print(triple_step_recurse(20))