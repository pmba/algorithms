totalFood = 0

size = int(input())

gameMap = [[0 for x in range(size)] for y in range(size)]

for i in range(size):
    gameMap[i] = input()

currentFood = 0

def runThroughMap(x, y, limit):
    global currentFood
    global totalFood

    if gameMap[y][x] == 'o':
        currentFood += 1
        if currentFood > totalFood:
            totalFood = currentFood
    elif gameMap[y][x] == 'A':
        currentFood = 0

    #print('[%d][%d]: %c' % (x, y, gameMap[y][x]))

    if x == limit-1 and y == limit-1:
        print(totalFood)
        return

    if y % 2 == 0:
        if x < limit - 1:
            runThroughMap(x+1, y, limit)
        else:
            runThroughMap(x, y+1, limit)
    else:
        if x > 0:
            runThroughMap(x-1, y, limit)
        else:
            runThroughMap(x, y+1, limit)

runThroughMap(0, 0, size)

        
        

    
