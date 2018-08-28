def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_in_array():
    assert 1 not in [2, 3, 4]


def test_str():
    assert 'fizz' in 'fizzbuss'
