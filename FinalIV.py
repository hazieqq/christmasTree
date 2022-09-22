
num_lines = int(input("Number of lines"))


totalStar = 1

stringStar = ""
stringTab = ""
    
for j in range(num_lines):
    for i in range(totalStar):
        stringStar += "*"
    for i in range(num_lines-j):
        stringTab += " "
    totalStar += 2
    print(stringTab+stringStar)
    stringStar = ""
    stringTab = ""

