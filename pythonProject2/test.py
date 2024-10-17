from lib import count_common_elements

def test_count_common_elements():
    assert count_common_elements([1, 2, 3], [2, 3, 4]) == 2
    assert count_common_elements([1, 2, 3], [4, 5, 6]) == 0
    assert count_common_elements([], [1, 2, 3]) == 0
    assert count_common_elements([1, 2, 3], [1, 2, 3]) == 3
    assert count_common_elements([1, 2], [2, 3], [2, 4]) == 1

if __name__ == "__main__":
    test_count_common_elements()
    print("Все тесты пройдены!")