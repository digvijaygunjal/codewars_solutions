clean = lambda text: "".join([c for c in text if c.islower() and text.count(c) > 1])

build_stat = lambda c, s1c, s2c: ('=:', s1c, c) if s1c == s2c else (('1:', s1c, c) if (s1c > s2c) else ('2:', s2c, c))

build_stats = lambda s1, s2: map(lambda char: build_stat(char, s1.count(char), s2.count(char)), set(s1 + s2))

sort = lambda stats: sorted(stats, key=lambda x: (-x[1], x[0], x[2]))

stat_as_text = lambda stat: stat[0] + (stat[2] * stat[1])

stats_as_text = lambda stat: map(stat_as_text, stat)


def mix(s1, s2):
    return "/".join(stats_as_text(sort(build_stats(clean(s1), clean(s2)))))
