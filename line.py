import math

pointA = (2, 2)
pointB = (10, 20)

def printArea(a: list):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[i][j]} ", end = "")
        print('', end = '\n')

def createArea(widthArea = 0, heightArea = 0):
    if widthArea == 0 and heightArea == 0:
        widthArea = int(input('Width: '))
        heightArea = int(input('Height: '))
    arrayArea = []
    for i in range(widthArea):
        arrayArea.append([])
        for j in range(heightArea): 
            arrayArea[i].append(".")
    return arrayArea

def renderLine(pointA, pointB, a: list, length: float):
    if pointA != pointB:
        stepX = round((pointB[0] - pointA[0]) / length, 3)
        stepY = round((pointB[1] - pointA[1]) / length, 3)
        x = pointA[0]
        y = pointA[1]
        while abs(round(x, 3)-pointB[0]) > abs(stepX) and abs(round(y, 3)-pointB[1]) > abs(stepY):
            x += stepX
            y += stepY
            a[round(x)][round(y)] = 'X'
            print(x, y, round(x), round(y))
    return a

def inputPoint():
    global testArea
    global pointA
    global pointB

    sizeY = int(input(f"Vector area horizontal size: "))
    sizeX = int(input(f"Vector area vertical size: "))
    testArea = createArea(sizeX, sizeY)
    x = int(input(f"PointA.x (0 - {sizeX - 1}): "))
    y = int(input(f"PointA.y (0 - {sizeY - 1}): "))
    pointA = (x,y)
    x = int(input(f"PointB.x (0 - {sizeX - 1}): "))
    y = int(input(f"PointB.y (0 - {sizeY - 1}): "))
    pointB = (x,y)
    testArea[pointA[0]][pointA[1]] = "X"
    testArea[pointB[0]][pointB[1]] = "X"
    lengthAB = math.sqrt((pointB[0]-pointA[0])*(pointB[0]-pointA[0]) + (pointB[1]-pointA[1])*(pointB[1]-pointA[1]))
    testArea = renderLine(pointA, pointB, testArea, lengthAB)
    printArea(testArea)
    print(f"Point A: {pointA}, Point B: {pointB}, Length AB: {lengthAB}")

if __name__ == "__main__":
    inputPoint()


