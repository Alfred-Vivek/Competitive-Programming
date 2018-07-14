def parenthesisCombination(n):
    result = []
    generateParenthesis(result, "", n, n)
    return result
def generateParenthesis(result, current, left, right):
    if left == 0 and right == 0:
        result.append(current)
    if left > 0:
        generateParenthesis(result, current + "(", left - 1, right)
    if left < right:
        generateParenthesis(result, current + ")", left, right - 1)

print (parenthesisCombination(2), len(parenthesisCombination(2)))
print (parenthesisCombination(3), len(parenthesisCombination(3)))
print (parenthesisCombination(5), len(parenthesisCombination(5)))
print (parenthesisCombination(4), len(parenthesisCombination(4)))
print (parenthesisCombination(1), len(parenthesisCombination(1)))
print (parenthesisCombination(6), len(parenthesisCombination(6)))