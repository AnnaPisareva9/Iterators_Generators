import types


def flat_generator(list_of_list):

    for list_ in list_of_list:
        for i in list_:
            if isinstance(i, list):
                for i_ in i:
                    while isinstance(i_, list):
                        for _ in i_:
                            if not isinstance(_, list):
                                i_ = _
                            else:
                                i_ = _
                    yield i_
            else:
                yield i


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()