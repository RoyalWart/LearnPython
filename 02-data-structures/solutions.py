def squares_of_evens(nums):
    return [n * n for n in nums if n % 2 == 0]


def second_largest(nums):
    return sorted(set(nums))[-2]


def unique_in_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def word_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def invert_dict(d):
    return {value: key for key, value in d.items()}


def common_elements(a, b):
    return sorted(set(a) & set(b))
