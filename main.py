import math

def PrimeList(N):
    primes = []
    for num in range(2, N):
        # 判断是否为质数
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 用空格连接列表元素，末尾无空格
    return ' '.join(primes)
