import main


def test_get_none():
    assert main.get_none() == None


def test_flatten_dict():
    assert type(main.flatten_dict({'a': 42, 'b': 3.14})) == list
    assert main.flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]
    assert type(main.flatten_dict({'a': [42, 350], 'b': 3.14})) == list
    assert main.flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]
    assert type(main.flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})) == list
    # assert main.flatten_dict(
    # {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [{'inner_a': 42, 'inner_b': 350}, 3.14]

    assert type(main.flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})) == list
    assert main.flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [42, 350, 3.14]

    assert type(main.flatten_dict({'a': [{'inner_inner_a': 42}]})) == list
    assert main.flatten_dict({'a': [{'inner_inner_a': 42}]}) == [42]
