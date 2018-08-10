def next_prime_number(num=2):
    next = ""
    while True:
        if not isPrime(num):
            for i in range(num + 1, (2 * num) + 1):
                if isPrime(i):
                    num = i
                    break
        print(num)
        num += 1
        next = input("If you would like to see the next number, press enter. If not, type anything and press enter. ")
        if len(next) != 0:
            print("End of program.")
            break


def isPrime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True


start = input("Choose a starting number. If no preference, just press enter. ")
if len(start) == 0:
    next_prime_number()
else:
    next_prime_number(int(start))
