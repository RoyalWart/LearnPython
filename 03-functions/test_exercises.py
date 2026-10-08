def test_total(ex):
    assert ex.total(1, 2, 3) == 6
    assert ex.total() == 0


def test_apply_twice(ex):
    assert ex.apply_twice(lambda n: n * 2, 3) == 12
    assert ex.apply_twice(str.upper, "a") == "A"


def test_make_multiplier(ex):
    double = ex.make_multiplier(2)
    triple = ex.make_multiplier(3)
    assert double(5) == 10
    assert triple(5) == 15


def test_build_profile(ex):
    assert ex.build_profile("Alex", age=16) == {"name": "Alex", "age": 16}
    assert ex.build_profile("Sam") == {"name": "Sam"}


def test_factorial(ex):
    assert ex.factorial(0) == 1
    assert ex.factorial(5) == 120


def test_sort_by_length(ex):
    assert ex.sort_by_length(["ccc", "a", "bb"]) == ["a", "bb", "ccc"]
