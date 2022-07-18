

def gettingInputFromCmdLine(number):
    x = range(number)
    retVal = [[]] * number
    for idx in x:
        retVal[idx] = int(input(f'"Please enter number({idx+1} of {x.stop}): "'))

    return retVal


def calculateMaxVal(inputList):
    maxVal = inputList[0]
    for idx in inputList:
        if maxVal < idx:
            maxVal = idx

    return maxVal


def main():
    inputList = gettingInputFromCmdLine(3)
    print(f'input list: {inputList}')
    maxVal = calculateMaxVal(inputList)
    print(f'Maximum Value: {maxVal}')


main()
