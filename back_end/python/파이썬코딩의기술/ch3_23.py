# -*- coding: utf-8 -*-


names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
#길이로 정렬
names.sort(key=lambda x: len(x))
print(names)


def log_missing():
    print('Key added')
    return 0


current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]

# 해당 객체가 생성될때 작동한다.
from collections import defaultdict

# current의 값이 불러질때마다 log_missing 를 호출
result = defaultdict(log_missing, current)
print('Before: ', dict(result))

for key, amount in increments:
    result[key] += amount

print('After: ', dict(result))


# 클로져로 변경
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)

    for key, amount in increments:
        result[key] += amount

    return result, added_count



current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]

result, count = increment_with_report(current, increments)
print(result, count)



# 클래스
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]

counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
print(counter.added)


# 클래스화 쫌더 좋은 방법
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]

counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
print(counter.added)
