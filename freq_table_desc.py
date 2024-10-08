from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequency')
    for number in table.most_common():
        print('{0}\t{1}'.format(number[0], number[1]))
if __name__=='__main__':
    scores = [7, 8, 8, 9, 9, 9]
    frequency_table(scores)
