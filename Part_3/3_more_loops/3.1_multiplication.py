# Write your solution here
number = int(input("Please type in a number:"))
first = 1

while first <= number:
    second = 1

    while second <= number:
        print(f"{first} x {second} = {first * second}")
        second += 1
    first += 1