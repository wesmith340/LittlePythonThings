# Assignment: HW-1a 
# Class: CS 701
# Author: Weston Smith
# Discount Facebook
# Description:  This application reads in a list of users from a file with friend connections to each other.
#               The application then can make recommendations on who a user should friend next.

# Main
def main():
    # User inputs the file
    fileName = input("Enter file name: ")

    # Read in file
    fileInput(fileName)

    # Show the network if possible
    showNetwork()

    msg = "Enter user id in the range 0 to " + str(numUsers-1) + " (-1 to quit) : "
    index = 0

    # Ask the user for indexes until they enter -1
    while index != -1:
        badData = True

        while badData:
            index = input(msg)

            # Check if the input is numeric and a valid number
            # Honestly though, why does isnumeric() not work with a negative?
            if str.isnumeric(index.strip("-")) == False or int(index)<-1 or int(index) >= numUsers:
                print("Error: Invalid Input")
            else:
                badData = False

        index = int(index)
        if index != -1:
            suggestUser(int(index))
        else:
            print("Goodbye!")

# Read in from a file
def fileInput(fileName):
    # Open file
    readFile = open(fileName, "r")

    global numUsers, userList
    numUsers = int(readFile.readline()) # Read in the number of users
    userList = tuple([set() for i in range(numUsers)]) # Create tuple of sets to store friend lists

    # Read in the rest of the file
    for i in readFile.readlines():
        fileInput = i.split()
        userList[int(fileInput[0])].add(int(fileInput[1]))
        userList[int(fileInput[1])].add(int(fileInput[0]))
    print("Finished reading File.\n")
    # Close the file
    readFile.close()

# Suggest a friend for the index passed in
def suggestUser(index):
    maxFriends = -1
    maxIndex = -1
    for i in range(numUsers):
        if i != index and i not in userList[index]:
            numMutual = len(userList[index].intersection(userList[i])) # Length of mutual friends
            if  numMutual > maxFriends:
                maxIndex = i
                maxFriends = numMutual
    print("The suggested friend for user",index,"is",maxIndex)

# Show network if possible
def showNetwork():
    if numUsers < 20:
        print("Network shown below")
        for i in range(numUsers):
            if len(userList[i]) > 0:
                print(i,":",userList[i])
            else:
                print(i,": {}")
    else:
        print("**Network representation too large to show**")
main()