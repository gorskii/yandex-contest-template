from solution import solve


cases = [
    ((0, 0, 0), 0),
    ((-1, 0, 1), 3),
]

for case, expected in cases:
    try:
        result = solve(*case)
        assert result == expected
        print("OK")
    except AssertionError:
        print('Given "{}".'.format(case))
        print('Got "{}".'.format(result))
        print('Expected "{}"'.format(expected))
        print()
