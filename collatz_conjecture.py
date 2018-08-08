def collatz_conjecture(n, count=0):
    if n == 1:
        return count
    if n % 2 == 0:
        return collatz_conjecture(n / 2, count + 1)
    else:
        return collatz_conjecture((n * 3) + 1, count + 1)
