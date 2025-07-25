

def add(first, second):
    return first+second

def sub(first, second):
    return first-second

def mul(first, second):
    return first*second

def div(first, second):
    return first/second

print("Input First Number:")
First= float(input())
print("Input First Number:")
Second= float(input())

print("Sum:" + str(add(First,Second)))
print("Sub:" + str(sub(First,Second)))
print("Product:" + str(mul(First,Second)))
print("Divident:" + str(div(First,Second)))
