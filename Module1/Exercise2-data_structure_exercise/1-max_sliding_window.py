def max_sliding_window(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        result.append(max(num_list[i:i+k]))
    return result

if __name__ == '__main__':
    num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
    k = 3
    print(max_sliding_window(num_list, k))