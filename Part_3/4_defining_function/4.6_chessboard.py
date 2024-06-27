def squared(s, n):
    length = len(s)
    row = 0
    while row < n:
        line = ""
        col = 0
        while col < n:
            line += s[(row + col) % length]
            col += 1
        print(line)
        row += 1
        
# Testing the function
if __name__ == "__main__":
    squared("cabca", 5)
