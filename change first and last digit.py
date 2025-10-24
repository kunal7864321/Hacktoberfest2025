def swap_first_last(num):
    a = num
    count = 0
    while a > 0:
        count += 1
        a //= 10
    p=(10 ** (count - 1))

    l = num % 10
    f= num // p
    m = (num % p) // 10
    result = l * p+ m * 10 + f
    return result
