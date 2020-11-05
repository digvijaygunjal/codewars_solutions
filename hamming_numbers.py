hamming_numbers = [1]
a, b, c = 2, 3, 5
i = j = k = 0


def resize_hamming_numbers(n):
    global hamming_numbers
    hamming_numbers = hamming_numbers + ([1] * (n - len(hamming_numbers)))


def hamming(n):
    global hamming_numbers, i, j, k, a, b, c
    # cached result
    if len(hamming_numbers) >= n:
        return hamming_numbers[n - 1]

    x, y, z = 2, 3, 5
    previous_length = len(hamming_numbers)
    resize_hamming_numbers(n)

    for l in range(previous_length, n):
        hamming_numbers[l] = min(a, b, c)
        if hamming_numbers[l] == a:
            i += 1
            a = x * hamming_numbers[i]
        if hamming_numbers[l] == b:
            j += 1
            b = y * hamming_numbers[j]
        if hamming_numbers[l] == c:
            k += 1
            c = z * hamming_numbers[k]

    return hamming_numbers[n - 1]
