total = 1
while True:
    try:
        num = int(input())
        total *= num
    except EOFError:
        break

print('Prod = %d' % total)
