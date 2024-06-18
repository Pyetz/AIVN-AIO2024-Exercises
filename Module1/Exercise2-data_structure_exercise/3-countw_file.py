def standardize_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.lower()
    content = content.replace('\n', ' ')
    return content

def count_chars (content):
    words = content.split()
    result = {}
    for char in words:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return dict(sorted(result.items()))

if __name__ == '__main__':
    file_path = 'AIVN-AIO2024-Exercises/Module1/Exercise2-data_structure_exercise/content/P1_data.txt'

    content = standardize_content(file_path)
    print(count_chars(content))