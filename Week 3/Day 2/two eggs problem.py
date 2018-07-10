neededDict = {}
def needed(eggs, floors):
    if (eggs, floors) in neededDict:
        return neededDict[(eggs, floors)]
    if eggs == 1:
        return floors
    if eggs > 1:
        minimum = floors
        for f in range(floors):
            resultIfEggBreaks = needed(eggs - 1, f)
            resultIfEggSurvives = needed(eggs, floors - (f + 1))
            result = max(resultIfEggBreaks, resultIfEggSurvives)
            if result < minimum:
                minimum = result
        neededDict[(eggs, floors)] = 1 + minimum
        return 1 + minimum
print (needed(2, 100))