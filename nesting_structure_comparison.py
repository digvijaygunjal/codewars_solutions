import collections

is_not_iterable = lambda e: not isinstance(e, collections.Iterable) or isinstance(e, type('string'))

is_iterable = lambda e: not is_not_iterable(e)

is_same_kind = lambda this, that: type(this) == type(that)

is_same_length = lambda this, that: len(this) == len(that)


def same_structure_as(this, that):
    if is_iterable(this) and is_iterable(that):
        return is_same_kind(this, that) and is_same_length(this, that) \
               and all(map(lambda x: same_structure_as(x[0], x[1]), zip(this, that)))
    return is_not_iterable(this) and is_not_iterable(that)
