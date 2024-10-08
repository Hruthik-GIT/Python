from collections import Counter
def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes


if __name__ == '__main__':
    scores = [7,8, 8, 8, 9, 9, 9]
    modes = calculate_mode(scores)
    print('The mode(s) of the list of numbers are:')
    for mode in modes: 
        print(mode)