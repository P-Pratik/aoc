t = 1000
sum = 0
for _ in range (t):
    string = input()
    num = ""
    for char in string:
        if char.isdigit():
            num += char
            break
    for char in string[::-1]:
        if char.isdigit():
            num += char
            break
    sum += int(num)
    
print(sum)