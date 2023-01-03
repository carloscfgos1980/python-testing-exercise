def get_none():
    return None


def flatten_dict(book):
    new_list = []
    for key, value in book.items():
        if type(value) == dict:
            print('value', value)
            c = list(value.values())
            new_list.append(c)
            # Check if is a Dictionary inside a list
        elif type(value) == list and type(value[0]) == dict:
            print('list-value:', value[0])  # checking the value
            x = str(value)  # turning the list into a string
            # slicing the string to isolate the number
            x = x[x.find(' ') + 1:-2]
            x = int(x)  # turning the string into a number
            new_list.append(x)
        else:
            print('simple values:', value)
            new_list.append(value)
    return new_list
