# def tribonacci(n):
#     if n <= 3:
#         return 1
#     else:
#         return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n  - 3)

def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}
    def tribonacci_rec(n):
        result = cache.get(n)
        if result is None:
            result = tribonacci_rec(n - 2) + tribonacci_rec(n - 1) + tribonacci_rec(n - 3)
            cache[n] = result
        return result
    return tribonacci_rec(n)

print(tribonacci(7))
