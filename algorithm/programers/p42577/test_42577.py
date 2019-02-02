
def test_42577():
    phone_book = ["119", "97674223", "1195524421"]
    assert False == solution(phone_book)

    phone_book = ["123", "456", "789"]
    assert True == solution(phone_book)

    phone_book = ["12", "123", "1235", "567", "88"]
    assert False == solution(phone_book)
