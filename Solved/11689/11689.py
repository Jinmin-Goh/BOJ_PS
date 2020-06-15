# Problem No.: 11689
# Solver:      Jinmin Goh
# Date:        20200614
# URL: https://www.acmicpc.net/problem/11689

import sys

# Euler's phi function

def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    
    temp = [True] * (10 ** 6 + 5)
    temp[0] = False
    temp[1] = False
    for i in range(2, 10 ** 6 + 5):
        if temp[i]:
            cnt = i * 2
            while cnt < 10 ** 6 + 5:
                temp[cnt] = False
                cnt += i
    primeList = []
    for i in range(2, 10 ** 6 + 5):
        if temp[i]:
            primeList.append(i)
    ans = n
    ansPrime = []
    for prime in primeList:
        if prime > n:
            break
        if n % prime == 0:
            ansPrime.append(prime)
            while n % prime == 0:
                n = n // prime
    if n != 1:
        ansPrime.append(n)

    n = ans
    # ans can be calculated with n(1 - 1/p1)(1 - 1/p2)...(1 - 1/pk)
    for i in range(1, 2 ** len(ansPrime)):
        temp = i
        tempPrime = []
        cnt = 0
        while temp > 0:
            if temp % 2:
                tempPrime.append(ansPrime[cnt])
            cnt += 1
            temp >>= 1
        mul = 1
        for i in tempPrime:
            mul *= i
            
        if len(tempPrime) % 2:
            ans -= n // mul
        else:
            ans += n // mul
    print(ans)
    

    return

if __name__ == "__main__":
    main()