# -*- coding: utf-8 -*-
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

# 이터레이터는 한번 읽으면 사라지므로
# 들어오자마자 list로 복사해서 사용
def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)

    return result


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result

if __name__ == '__main__':
    visits = [15, 35, 80]
    percentages = normalize(visits)
    print(percentages)

    # 이터레이터는 한번 읽으면 사라짐
    it = read_visits('./my_numbers.txt')
    print(list(it))
    print(list(it))
    percentages = normalize(it)
    print(percentages)

    # 이터레이터를 복사해서 사용 ( 이터레이터를 사용 이유가 사라짐)
    it = read_visits('./my_numbers.txt')
    percentages = normalize_copy(it)
    print(percentages)

    # lamdba로 넘겨주면 이터레이터를 계속해서 쓸수 있다.
    percentages = normalize_func(lambda: read_visits('./my_numbers.txt'))
    print(percentages)

    # 다 좋지만 입력 데이터를 여러번 읽게 된다. (class에서__iter__를 통해 이터레이터를 접근하는데, normalize에서 읽을시 매번 새로운 이터레이터로 반환됨)
    visits = ReadVisits('./my_numbers.txt')
    percentages = normalize(visits)
    print(percentages)

    # 리스트 이터레이터 둘다 작동하도록
    percentages = normalize_defensive([15, 35, 80])
    print(percentages)
    visits = ReadVisits('./my_numbers.txt')
    percentages = normalize_defensive(visits)
    print(percentages)
