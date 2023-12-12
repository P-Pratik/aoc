t = 1000
sum = 0
value = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
rvalue = {"eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9"}

for _ in range (t):
    string = input()
    rstring = string[::-1]
    num = ""
    for char in string:
        if char.isdigit():
            index = string.index(char)
            digit = char
            break
    for i in value:
        curr = 1000
        if string.find(i) != -1:
            curr = string.index(i)
        if curr < index:
            index = curr
            digit = value[i]
    num += digit
    
    for char in rstring:
        if char.isdigit():
            index = rstring.index(char)
            digit = char
            break
    for i in rvalue:
        curr = 1000
        if rstring.find(i) != -1:
            curr = rstring.index(i)
        if curr < index:
            index = curr
            digit = rvalue[i]
    num += digit
    sum += int(num)
    
print(sum)