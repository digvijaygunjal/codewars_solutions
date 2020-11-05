def smallest_number(tenth, unit, discarded):
    rest = [unit] + discarded
    greater_than_tenth = sorted(list(filter(lambda x: x > tenth, rest)))
    smaller_than_tenth = list(filter(lambda x: x <= tenth, rest))
    if len(greater_than_tenth) == 0:
        return [unit] + sorted([tenth] + discarded)
    else:
        return greater_than_tenth[:1] + sorted([tenth] + greater_than_tenth[1:] + smaller_than_tenth)


def next_bigger(n):
    digits = list(str(n))
    discarded = []
    while len(digits) >= 2:
        ten, unit = digits[-2:]
        if int(unit) > int(ten):
            return int("".join(digits[:-2] + smallest_number(ten, unit, discarded)))
        discarded.append(digits.pop())
    return -1
