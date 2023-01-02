import main


def test_get_none():
    assert main.get_none() == None


def flatten_dict(book):
    outcome = list(book.values())
    print(outcome)
    return outcome


print(flatten_dict({'a': [42, 350], 'b': 3.14}))


def test_flatten_dict():
    assert type(flatten_dict({'a': 42, 'b': 3.14})) == list
    assert flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]
    assert type(flatten_dict({'a': [42, 350], 'b': 3.14})) == list
    assert flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]
    assert type(flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})) == list
    assert flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [{'inner_a': 42, 'inner_b': 350}, 3.14]

    assert type(flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})) == list
    assert flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [42, 350, 3.14]

    assert type(flatten_dict({'a': [{'inner_inner_a': 42}]})) == list
    assert flatten_dict({'a': [{'inner_inner_a': 42}]}) == [42]
