from functools import wraps


stor_items = {}
stor_names = []


def prost_get_items(stor):
    def get_items(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            stor[func.__name__] = res
            return res
        return wrapper
    return get_items


def prost_get_name(stor):
    def get_items(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            stor.append(func.__name__)
            return res
        return wrapper
    return get_items


@prost_get_name(stor_names)
@prost_get_items(stor_items)
def get_sum(*args, **kwargs):
    return sum(a for a in args)


@prost_get_name(stor_names)
@prost_get_items(stor_items)
def get_print(*args, **kwargs):
    return (args)


@prost_get_name(stor_names)
@prost_get_items(stor_items)
def get_even(*args, **kwargs):
    return [a for a in range(*args) if a % 2 == 0]


@prost_get_items(stor_items)
def get_pow(a, b):
    return a**b


@prost_get_items(stor_items)
def get_cont(a, b):
    return '{0}{1}'.format(a, b)


get_sum(22, 4, 1)
get_print("hello belyash")
get_pow(2, 8)
get_cont("213", " papy")
get_even(20)

print(stor_items)
print(stor_names)

print(get_sum(22, 4, 1))
