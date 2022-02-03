"""
Question 1: Love Nines

Given a number N, find out minimum number of numbers needed whose last digit is 9 to make sum N. Output -1 if not possible.

Examples:
209 => Output: 1 (209's last digit is 9)
37 => Output: 3 (19 + 9 + 9)

"""
def nines(n):
    l = n % 10
    m = n // 10
    if (9 - l <= m):
        return 10 - l
    else:
        return -1

print(nines(209))