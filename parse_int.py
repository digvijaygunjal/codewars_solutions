from functools import reduce

units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
         'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

values = {}
for i, word in enumerate(units): values[word] = i
for i, word in enumerate(tens): values[word] = i * 10

multipliers = {
    "million": 1000000,
    "thousand": 1000,
    "hundred": 100
}

get_sentences = lambda string, scale: string.replace(scale, scale + ";").split(';')
get_lhs_rhs = lambda sentences: (" ".join("".join(sentences[:-1]).split(' ')[:-1]), "".join(sentences[-1:]))
get_words = lambda string: string.strip().replace('-', ' ').split(' ')
add = lambda words: reduce(lambda x, y: x + values.get(y, 0), words, 0)


def parse_int(string):
    words = get_words(string)
    for scale in multipliers.keys():
        if words.count(scale) > 0:
            lhs, rhs = get_lhs_rhs(get_sentences(string, scale))
            return parse_int(lhs) * multipliers[scale] + parse_int(rhs)

    return add(words)
