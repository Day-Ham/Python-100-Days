randomNumbers = [37, 92, 15, 68, 43, 84, 29, 10, 56, 77, 61, 24, 89, 7, 48, 33, 95, 12, 73, 50];
maxScore=0

for score in randomNumbers:
    if score>maxScore:
        maxScore=score
print(maxScore)
print("Before Sort")
print( randomNumbers)
randomNumbers.sort()
print("After Sort")
print(randomNumbers)
