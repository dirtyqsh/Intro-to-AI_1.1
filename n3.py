def is_prime(num):
    flag = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            flag = False
            break
    if flag:
        return flag
    else:
        return flag