"""
Dada uma lista de números inteiros nums e um número alvo target, retorne os índices (posições) dos dois números que
somados resultam no target.
"""


def two_sum(nums, target):
    p = nums.copy()
    for i, num in enumerate(nums):
        p[i] = ""
        t = target - num
        if t in p:
            return [i,p.index(t)]
    return []

# Teste

print(two_sum([2, 7, 11, 15],9))
print(two_sum([3, 2, 4], 6))
print(two_sum([-5,-1, -2],-7))