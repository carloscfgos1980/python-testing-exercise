def get_none():
    return None


def flatten_dict(book):
    for key, value in book.items():
        if type(value) == dict:
            print('key', key)
            print('value', value)
            c = list(value.values())
            return c
            # Check if is a Dictionary inside a list
        elif type(value) == list:
            print('list-value:', value)  # checking the value
            x = str(value)  # turning the list into a string
            # slicing the string to isolate the number
            x = x[x.find(' ') + 1:-2]
            x = [int(x)]  # turning the string into a number
            return x
        else:
            d = list(book.values())
            return d
