def factorial (n):
    if n < 2:
        return 1
    return n * factorial(n-1)

def approx_sin(x, n):
    result = 0
    for i in range (0, n + 1):
        result += (-1)**i * (x**(2*i+1) / factorial(2*i+1))
    return result

def approx_cos(x, n):
    result = 0
    for i in range (0, n + 1):
        result += (-1)**i * (x**(2*i) / factorial(2*i))
    return result

def approx_sinh(x, n):
    result = 0
    for i in range (1, 2*n + 2, 2):
        result += x**(i) / factorial(i)
    return result

def approx_cosh(x, n):
    result = 0
    for i in range (0, 2*n + 1, 2):
        result += (x**(i) / factorial(i))
    return result

if __name__ == '__main__':
    x = input('enter radian: ')
    try:
        x = float(x)
        n = input('enter a positive integer: ')
        try:
            n = int(n)
            if n > 0:
                print(approx_sin(x, n))
                print(approx_cos(x, n))
                print(approx_sinh(x, n))
                print(approx_cosh(x, n))
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)