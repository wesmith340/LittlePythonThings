# Assignment: HW-1b 
# Class: CS 701
# Author: Weston Smith
# Dicount Pacman
# Description:  This application is a command line fascimile of Pacman. Where a user is able to move, 
#               turn left or right, and consume items without any of the skill or tension actual Pacman requires

# Main
def main():
    fileName = "init_grid.txt"
    inputFile(fileName) # Input file
    global toggleShow, path
    toggleShow = True

    path = set() # Set of coordinates that have been traveled

    displayGrid() # Display the grid

    welcome = ["-----Welcome to Pacman-----","  L:   Turn Left","  R:   Turn Right","[x]:   Move x number of steps",
                "  C:   Consume Item","  P:   Place Item","  S:   Show/Hide Path", "  Q:   Quit"]
    print("\n".join(welcome)) # Output welcome message

    userInput = "welcome"
    while userInput != "Q":
        # Get user input
        userInput = str.upper(input())
        processInput(userInput)

#------------------------------------------------------------------------------------------------------------------------
#   User Input
def processInput(userInput):
    if userInput == "Q": # Quit
        return None
    if userInput == "L": # Turn Left
        turnLeft()
    elif userInput == "R": # Turn Right
        turnRight()
    elif str.isnumeric(userInput):
        if checkMove(int(userInput)): # Move forward
            move(int(userInput)) 
        else:
            print("Invalid move. Enter again")
            return None
    elif userInput == "C": # Consume Item
        consumeItem()
    elif userInput == "P": # Place Item
        placeItem()
    elif userInput == "S": # Toggle the path
        global toggleShow
        toggleShow = toggleShow == False
    else:                  # Invalid input
        print("Error: Invalid Input")
    displayGrid()
#------------------------------------------------------------------------------------------------------------------------
#    Input from file
def inputFile(fileName):
    global grid, xMax, yMax, direction, xCur, yCur

    fileReader = open(fileName, "r")
    line = fileReader.readline().split()

    yMax = int(line[0])
    xMax = int(line[1])

    # Create grid of .'s
    grid = [["." for k in range(xMax)] for j in range(yMax)]

    # Read in initial start point
    start = fileReader.readline().split()
    yCur = int(start[0])
    xCur = int(start[1])

    # Read in initial direction
    line = fileReader.readline()

    if line == "N\n":
        grid[int(start[0])][int(start[1])] = "^"
        direction = "N"
    elif line == "E\n":
        grid[int(start[0])][int(start[1])] = ">"
        direction = "E"
    elif line == "W\n":
        grid[int(start[0])][int(start[1])] = "<"
        direction = "W"
    elif line == "S\n":
        grid[int(start[0])][int(start[1])] = "v"
        direction = "S"

    # Read in obstacles
    numObs = int(fileReader.readline())

    for i in range(numObs):
        line = fileReader.readline().split()
        grid[int(line[0])][int(line[1])] = "x"

    # Read in items
    numItems = int(fileReader.readline())

    for i in range(numItems):
        line = fileReader.readline().split()
        grid[int(line[0])][int(line[1])] = "o"
    
    print("	Finished reading initial grid from file.")
#------------------------------------------------------------------------------------------------------------------------
#   Turning methods
def turnLeft():
    global direction
    fixAfter = False
    if grid[yCur][xCur] == "@": # If pacman is on an item, make sure to replace the item after turning
        fixAfter = True

    if direction == "N":
        direction = "W"
        grid[yCur][xCur] = "<"
    elif direction == "W":
        direction = "S"
        grid[yCur][xCur] = "v"
    elif direction == "S":
        direction = "E"
        grid[yCur][xCur] = ">"
    elif direction == "E":
        direction = "N"
        grid[yCur][xCur] = "^"

    if fixAfter == True: # Replace the item if needed
        grid[yCur][xCur] = "@"
    
def turnRight():
    global direction
    fixAfter = False
    if grid[yCur][xCur] == "@": # If pacman is on an item, make sure to replace the item after turning
        fixAfter = True

    if direction == "N":
        direction = "E"
        grid[yCur][xCur] = ">"
    elif direction == "E":
        direction = "S"
        grid[yCur][xCur] = "v"
    elif direction == "S":
        direction = "W"
        grid[yCur][xCur] = "<"
    elif direction == "W":
        direction = "N"
        grid[yCur][xCur] = "^"

    if fixAfter == True: # Replace the item if needed
        grid[yCur][xCur] = "@"
#------------------------------------------------------------------------------------------------------------------------
#   Movement functions
def checkMove(numMove): # Checks if move is valid
    goodMove = True
    column = []
    for i in grid:
        column.append(i[xCur])

    if (numMove <= 0):
        goodMove = False
    elif direction == "N" and (yCur - numMove < 0 or "x" in column[yCur:yCur-numMove:-1]):
        goodMove = False
    elif direction == "E" and (xCur + numMove > xMax-1 or "x" in grid[yCur][xCur:xCur+numMove:1]):
        goodMove = False
    elif direction == "S" and (yCur + numMove > yMax-1 or "x" in column[yCur:yCur+numMove:1]):
        goodMove = False
    elif direction == "W" and (xCur - numMove < 0 or "x" in grid[yCur][xCur:xCur-numMove:-1]):
        goodMove = False
    return goodMove

def move(numMove): # Move numMove number of spaces
    global yCur,xCur, path
    yNext = yCur
    xNext = xCur
    n = 0
    if grid[yCur][xCur] == "@": # If Pacman is on item, make sure not to delete it
        n = 1
        grid[yCur][xCur] = "o"

    if direction == "N": # Move up
        yNext = yCur-numMove
        if grid[yNext][xCur] == "o":
            grid[yNext][xCur] = "@"
        else:
            grid[yNext][xCur] = "^"

        for i in range(yCur-n,yNext,-1):
            path.add((xCur, i))

    elif direction == "E": # Move right
        xNext = xCur + numMove
        if grid[yCur][xNext] == "o":
            grid[yCur][xNext] = "@"
        else:
            grid[yCur][xNext] = ">"

        for i in range(xCur+n,xNext,1):
            path.add((i, yCur))

    elif direction == "S": # Move down
        yNext = yCur+numMove
        if grid[yNext][xCur] == "o":
            grid[yNext][xCur] = "@"
        else:
            grid[yNext][xCur] = "v"

        for i in range(yCur+n,yNext,1):
            path.add((xCur, i))

    elif direction == "W": # Move left
        xNext = xCur - numMove
        if grid[yCur][xNext] == "o":
            grid[yCur][xNext] = "@"
        else:
            grid[yCur][xNext] = "<"

        for i in range(xCur-n,xNext,-1):
            path.add((i, yCur))

    yCur = yNext
    xCur = xNext
#------------------------------------------------------------------------------------------------------------------------
#   Item methods
def consumeItem(): # Consume an item
    if grid[yCur][xCur] == "@":
        if direction == "N":
            grid[yCur][xCur] = "^"
        elif direction == "E":
            grid[yCur][xCur] = ">"
        elif direction == "S":
            grid[yCur][xCur] = "v"
        elif direction == "W":
            grid[yCur][xCur] = "<"
    else:
        print("There is nothing to C O N S U M E . . .")

def placeItem(): # Place an item
    global xCur, yCur
    grid[yCur][xCur] = "@"
#------------------------------------------------------------------------------------------------------------------------
# Display the grid
def displayGrid():
    print("Grid Looks Like:")
    if toggleShow: # If path is supposed to be showing
        for i in path:
            if(i[0] != xCur or i[1] != yCur):
                grid[i[1]][i[0]] = " "

    else: # If path is supposed to be hidden
        for i in path:
            if(i[0] != xCur or i[1] != yCur):
                grid[i[1]][i[0]] = "."

    display = "\n".join([" ".join(r) for r in grid])
    print(display)


main()