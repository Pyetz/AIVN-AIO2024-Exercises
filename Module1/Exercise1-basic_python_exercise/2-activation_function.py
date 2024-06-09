import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    
    return True

def sigmoid(x):
    return 1 / (1 + math.pow(math.e, -x))

def relu(x):
    if x <= 0:
        return 0.0
    else:
        return x

def elu(x):
    alpha = 0.01
    if x <= 0:
        return alpha * (math.e**x - 1)
    else:
        return x
    
if __name__ == '__main__':
    x = input('enter x: ')
    if (is_number(x)):
        x = float(x)
        activate_function = input('enter activate function name: ')
        if activate_function in ('sigmoid', 'relu', 'elu'):
            if activate_function == 'sigmoid':
                print(sigmoid(x))
            elif activate_function == 'relu':
                print(relu(x))
            else:
                print(elu(x))
        else:
            print(activate_function, 'is not supported')
    else:
        print('x must be a number')