def solution(phone_book):
    d = {}
    for phone in phone_book:
        for key in d.keys():
            print(key, phone, key.find(phone))
            if key.find(phone) == 0 or phone.find(key) == 0:
                return False
        d[phone] = 0

    return True

