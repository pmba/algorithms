global feedSize
feedSize = int(input())
friendsSize = int(input())

proximities = [0 for i in range(friendsSize)]

for i in range(friendsSize):
    friendIndex, proximity = input().split()
    proximities[int(friendIndex)-1] = float(proximity)

postsSize = int(input())

posts = [[0 for i in range(3)] for j in range(postsSize)]

for i in range(postsSize):
    info = input().split(' ')
    
    friendIndex = info[0]
    info.remove(info[0])
    
    time = info[0]
    info.remove(info[0])
    
    message = " ".join(info)
    
    priority = 0.8*proximities[int(friendIndex)-1]+0.2*float(time)
    posts[i][0] = priority
    posts[i][1] = int(friendIndex)
    posts[i][2] = message

def quickSort(lista):
    if lista:
        left = [x for x in lista if x[0] > lista[0][0]]
        right = [x for x in lista if x[0] < lista[0][0]]
        if len(left) > 1:
            left = quickSort(left)
        if len(right) > 1:
            right = quickSort(right)
        return left + [lista[0]] * lista.count(lista[0]) + right
    return []

sortedPosts = quickSort(posts)

for i in range(feedSize):
    print(str(sortedPosts[i][1]) + ' ' + sortedPosts[i][2]) 
