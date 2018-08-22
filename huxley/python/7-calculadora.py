total = float(input())
num1 = float(input())
operation = input()

if operation == '+':
    total = total + num1
    print('%.3f' % total)
elif operation == '-':
    total = total - num1
    print('%.3f' % total)
elif operation == '/':
    if num1 != 0:
        total = total / num1
        print('%.3f' % total)
    else:
        print('operacao nao pode ser realizada')
elif operation == '*':
    total = total * num1
    print('%.3f' % total)

while operation != '&':
    num1 = float(input())
    operation = input()

    if operation == '&':
        break
    elif operation == '+':
        total = total + num1
        print('%.3f' % total)
    elif operation == '-':
        total = total - num1
        print('%.3f' % total)
    elif operation == '/':
        if num1 != 0:
            total = total / num1
            print('%.3f' % total)
        else:
            print('operacao nao pode ser realizada')
    elif operation == '*':
        total = total * num1
        print('%.3f' % total)

    
        
