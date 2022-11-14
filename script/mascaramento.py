# Example number:
number = '123456789'

# Leave only last two/three/four digits:
lastTwo = number[-2:]
lastThree = number[-3:]
lastTFour = number[-4:]

print(lastTwo)    # 89
print(lastThree)  # 789
print(lastTFour)  # 6789

# Mask number leaving only last two/three/four digits:
maskedNumber1 = lastTwo.rjust(len(number), '*')
maskedNumber2 = lastThree.rjust(len(number), '*')
maskedNumber3 = lastTFour.rjust(len(number), '*')

print(maskedNumber1)  # *******89
print(maskedNumber2)  # ******789
print(maskedNumber3)  # *****6789
