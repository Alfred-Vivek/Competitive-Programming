def can_two_movies_fill_flight(movie_lengths, flight_length):
    watch = {}
    for x in movie_lengths:
        c = flight_length-x
        if c in watch:
            return True
        else:
            watch[x] = True
    return False

# Test Cases

result = can_two_movies_fill_flight([2, 4], 1)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([2, 4], 6)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([3, 8], 6)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([3, 8, 3], 6)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([6], 6)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([], 2)
expected = False
print(result == expected)
