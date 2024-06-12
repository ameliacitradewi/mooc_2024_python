# Write your solution here
password = input("Password:")

while True:
    repeat = input("Repeat password:")

    if repeat != password:
        print("They do not match!")
    else:
        print("User account created!")
        break