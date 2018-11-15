def add(a, b):
    # If we add two digits, the larger of the two numbers is kept.
    if a not is
    a, b = str(a), str(b)  # Convert integers to string so that we can look at each digit.


    # Part 1: If one number has more digits than another, we can simply carry down the extra digits to the final sum.
    digitsA, digitsB = len(a), len(b)
    digitDif = abs(digitsA - digitsB)

    # The following if and else statements carry down any extra digits directly into the sum and remove those digits from the number.
    sum = ""
    if digitsA > digitsB:
        sum, a = a[:digitDif], a[digitDif:]
    elif digitsB > digitsA:
        sum, b = b[:digitDif], b[digitDif:]
    digits = digitsA if digitsA < digitsB else digitsB # We modified the longer number, so now they have the same number of digits.


    # Part 2: Proceed through each digit of the two numbers and carry down the larger of the two numbers.
    for currentDigit in range(0, digits):
        if a[currentDigit] > b[currentDigit]:
            sum += a[currentDigit]
        else:
            sum += b[currentDigit]
    return int(sum)

def mul(a, b):
    a, b = str(a), str(b)

    previousResult = "0"
    digitsA, digitsB = len(a), len(b)
    for x in range(0, digitsB):
        currentResult = ""
        numberOfZerosFromB = digitsB-1-x
        for y in range(0, digitsA):
            numberOfZeroesFromA = digitsA-1-y
            currentResult += a[y] if a[y] < b[x] else b[x]
        currentResult += "0" * numberOfZerosFromB
        result = add((currentResult), previousResult)
        previousResult = result
    return int(result)

