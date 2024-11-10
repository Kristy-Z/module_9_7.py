def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_prime_decorator(func_decorate):
    def wrapper(*args, **kwargs):
        result = func_decorate(*args, **kwargs)
        if is_prime(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime_decorator
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
