clean = lambda text: "".join([c for c in text if c.islower()])

build_stats = lambda s1, s2: map(lambda c: get_stats(c, s1, s2), set(s1 + s2))

remove_singles = lambda stats: filter(lambda x: x[1] > 1, stats)

sort = lambda stats: sorted(stats, key=lambda x: (-x[1], x[0], x[2]))

build_from_stat = lambda x: x[0] + (x[2] * x[1])


def get_stats(c, s1, s2):
    s1c, s2c = s1.count(c), s2.count(c)
    return ('=:', s1c, c) if s1c == s2c else (('1:', s1c, c) if (s1c > s2c) else ('2:', s2c, c))


def mix(s1, s2):
    sorted_pairs = sort(remove_singles(build_stats(clean(s1), clean(s2))))
    return "/".join(map(build_from_stat, sorted_pairs))
