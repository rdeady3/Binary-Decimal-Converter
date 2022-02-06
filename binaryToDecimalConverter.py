"""
Russell Deady
Program I made to convert back and forth between binary and decimal numbers
"""

def main(): 
    
    valueList = []
    flag1 = False
    flag2 = False
    binaryNumber = 0
    decimalNumber = 0
    
    print()
    print("Are you converting a binary number or a decimal number?")
    startingType = input("Enter the character 'b' for binary or the character 'd' for decimal: ")

    # handle case where user is going from binary to decimal
    if (startingType == 'b'):
        binaryNumber = input("Enter the binary number to convert: ")
        numLength = len(binaryNumber)
        power = numLength - 1
        i = 0
        while (i < numLength ):
            if (int(binaryNumber[i]) % 2 == 0):
                power = power - 1
                i = i + 1
                continue
            elif (int(binaryNumber[i]) % 2 == 1):
                decimalNumber = decimalNumber + pow(2,power)
            i = i + 1
            power = power - 1

        flag1 = True
    # handle case where user is going from decimal to binary 
    elif (startingType == 'd'):
        decimalNumber = input("Enter the decimal number to convert: ")
        num = int(decimalNumber)
        valueList.append(num % 2)
        while (num > 1):
            valueList.append(num % 2)
            num = num // 2
        
        valueList.append(num % 2)

        flag2 = True
    else:
        print()
        print("Incorrect input, enter a 'b' or a 'd' next time!")
        print()
        return

    if (flag1 == True):
        print()
        print("The decimal number is",decimalNumber)
    elif (flag2 == True):
        print()
        print("The binary number is...")
        i = len(valueList) - 1
        while (i > 0):
            print(valueList[i], end="")
            i = i - 1
        print()

    
    print()
    return

main()
