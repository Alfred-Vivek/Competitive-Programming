def get_max_profit(stock_prices):

	if len(stock_prices) < 2:
		raise ValueError('Data Not Sufficient')
	minimum = stock_prices[0]
	maximum = stock_prices[1] - stock_prices[0]
	for x in range(1,len(stock_prices)):
		i = stock_prices[x]
		profit = i - minimum
		maximum = max(profit, maximum)
		minimum = min(minimum,i)    
	return maximum

# Tests Cases

actual = get_max_profit([1, 5, 3, 2])
expected = 4
print(actual == expected)

actual = get_max_profit([7, 2, 8, 9])
expected = 7
print(actual == expected)

actual = get_max_profit([1, 6, 7, 9])
expected = 8
print(actual == expected)

actual = get_max_profit([9, 7, 4, 1])
expected = -2
print(actual == expected)

actual = get_max_profit([1, 1, 1, 1])
expected = 0
print(actual == expected)