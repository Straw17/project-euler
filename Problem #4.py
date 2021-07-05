def reverse(s):
    string = ''
    for i in s:
        string = i + string
    return string

highestPal = 0
for num1 in range(999, 100, -1):
    for num2 in range(999, 100, -1):
        num = num1 * num2
        if str(num) == reverse(str(num)) and num > highestPal:
            highestPal = num
print(highestPal)
        
    
