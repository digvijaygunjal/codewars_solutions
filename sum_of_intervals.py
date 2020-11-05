from functools import reduce


def is_between(number, numbers):
    return numbers[0] <= number < numbers[1]


def is_overlapping(one, two):
    return is_between(one[0], two) or is_between(one[1], two) or is_between(two[0], one) or is_between(two[1], one)


def create_max_range(ranges):
    return min(map(lambda x: x[0], ranges)), max(map(lambda x: x[1], ranges))


def find_all_overlapping(i, non_overlapping_intervals):
    return list(filter(lambda x: is_overlapping(i, x), non_overlapping_intervals))


def remove_from(intervals, to_remove):
    return [i for i in intervals if i not in to_remove]


def non_overlapping(intervals):
    non_overlapping_intervals = []
    for interval in intervals:
        overlapping_intervals = find_all_overlapping(interval, non_overlapping_intervals)
        if len(overlapping_intervals) > 0:
            non_overlapping_intervals = remove_from(non_overlapping_intervals, overlapping_intervals)
            non_overlapping_intervals.append(create_max_range([interval] + overlapping_intervals))
        else:
            non_overlapping_intervals.append(interval)
    return non_overlapping_intervals


def sum_of_intervals(intervals):
    return reduce(lambda res, interval: res + (interval[1] - interval[0]), non_overlapping(intervals), 0)
