def count_big(numbers, limit):
    count = 0
    for num in numbers:
        if num >= limit:
            count += 1
    return count

numbers = [2, 5, 3]
print(count_big(numbers, 2))
