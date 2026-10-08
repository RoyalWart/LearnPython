def test_squares_of_evens(ex):
    assert ex.squares_of_evens([1, 2, 3, 4]) == [4, 16]
    assert ex.squares_of_evens([1, 3]) == []


def test_second_largest(ex):
    assert ex.second_largest([5, 1, 9, 9, 3]) == 5
    assert ex.second_largest([1, 2]) == 1


def test_unique_in_order(ex):
    assert ex.unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert ex.unique_in_order([]) == []


def test_word_count(ex):
    assert ex.word_count("the cat and The dog") == {
        "the": 2, "cat": 1, "and": 1, "dog": 1}


def test_invert_dict(ex):
    assert ex.invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_common_elements(ex):
    assert ex.common_elements([1, 2, 2, 3], [2, 3, 4]) == [2, 3]
    assert ex.common_elements([1], [2]) == []
