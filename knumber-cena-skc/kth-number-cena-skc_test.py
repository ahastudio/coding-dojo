def partlist(array, command):
    return knumber(sorting(partlist2(array, command)), command[2])


def partlist2(array, command):
    return array[command[0] - 1: command[1]]


def sorting(part):
    return sorted(part)


def knumber(sorted, k):
    return sorted[k - 1]


def solution(array, commands):
    return [partlist(array, commands[i]) for i in range(len(commands))]


def test_partlist():
    assert partlist([1, 5, 2, 6, 3, 7, 4], [2, 5, 3]) == 5
    assert partlist([1, 5, 2, 6, 3, 7, 4], [4, 4, 1]) == 6


def test_solution():
    assert solution([1, 5, 2, 6, 3, 7, 4],
                    [
                        [2, 5, 3],
                        [4, 4, 1],
                        [1, 7, 3]
                    ]
                    ) == [5, 6, 3]

    assert solution([9, 8, 7, 6, 5, 4],
                    [
                        [2, 5, 3],
                        [4, 4, 1],
                        [1, 6, 3]
                    ]
                    ) == [7, 6, 6]


def test_partlist2():
    assert partlist2([1, 5, 2, 6, 3, 7, 4], [2, 5, 3]) == [5, 2, 6, 3]
    assert partlist2([1, 5, 2, 6, 3, 7, 4], [4, 4, 1]) == [6]
    assert partlist2([1, 5, 2, 6, 3, 7, 4], [1, 7, 3]) == [1, 5, 2, 6, 3, 7, 4]


def test_sorting():
    assert sorting([5, 2, 6, 3]) == [2, 3, 5, 6]
    assert sorting([1, 5, 2, 6, 3, 7, 4]) == [1, 2, 3, 4, 5, 6, 7]


def test_knumber():
    assert knumber([2, 3, 5, 6], 3) == 5
