Chequea con el pytest que hay algo que me da error... si tienes tiempo claro

Este es lo que piden en el ejercicio

Part 2

In test_main.py, write a function test_flatten_dict that tests if a function flatten_dict, when given a dictionary (dict) as its argument, returns the values of that dictionary in a list (list). For example:

flatten_dict({'a': 42, 'b': 3.14})
# [42, 3.14]
flatten_dict({'a': [42, 350], 'b': 3.14})
# [[42, 350], 3.14]
Tip

Try to think about the tests you're writing as a tiered system. First you might test if the value returned by flatten_dict is a list at all. Then you could test the function with a very small (single element) dictionary, then more complex dictionaries. This way, if a test fails, you not only now that it fails, but also exactly where it fails. The more granular your testing tiers, the better you can trace the bug if the test fails.

In main.py, implement the function flatten_dict so that it passes the tests you wrote in test_flatten_dict. Another example:

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
# [{'inner_a': 42, 'inner_b': 350}, 3.14]
Run the tests you wrote with pytest as you are working on the implementation of the flatten_dict function.

Note

For an extra challenge, see if you can implement flatten_dict in such a way that the dictionary is flattened all the way down regardless of how many nested levels original dictionary contains. For example:

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
# [42, 350, 3.14]
flatten_dict({'a': [{'inner_inner_a': 42}]})
# [42]
To do this you may want to look into a technique that is called recursion
