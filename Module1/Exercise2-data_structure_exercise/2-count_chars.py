def count_chars (word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return dict(sorted(result.items()))

if __name__ == '__main__':
    string = 'Happiness'
    print(count_chars(string))

    string = 'smiles'
    print(count_chars(string))