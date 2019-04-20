# -*- coding: utf-8 -*-

def index_words(text):
    result = []
    if text:
        result.append(0)

    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

# 이터레이터를 사용하자!!
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


if __name__ == '__main__':
    address = 'Four score and seven years ago...'
    result = index_words(address)
    print(result)

    result = index_words_iter(address)
    print([x for x in result])

    with open('./address.txt', 'r') as f:
        it = index_file(f)
        print([x for x in it])
        
    
