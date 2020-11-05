def solution(args):
    final = []
    n = 0
    while n < len(args):
        r = list(map(lambda x: str(x), get_range(args, n)))
        if len(r) >= 3:
            final.append(str(r[0]) + '-' + str(r[len(r) - 1]))
        else:
            final = final + r
        n += len(r)

    return ",".join(final)


def get_range(args, index):
    result = [args[index]]
    index += 1
    while index < len(args):
        if abs(args[index] - args[index - 1]) == 1:
            result.append(args[index])
            index += 1
        else:
            return result
    return result
