# Assignment: HW-2 
# Class: CS 697
# Author: Weston Smith
# Employment Numbers
# Description:  This application reads in data about presidents and job data related to years and formats them 



import matplotlib.pyplot as plt

#Main
def main():

    presidents = getPresidents("presidents.txt")    # Read in president data
    priData = getData("private.csv")                # Read in private employment data
    govData = getData("gov.csv")                    # Read in government employment data

    # Average monthly data for Private and Government data
    print("\nPrivate employment average per month (thousands)")
    aveMonthly(priData, presidents)
    print("\nGovernment employment average per month (thousands)")
    aveMonthly(govData, presidents)
    
    # Private and Government data by president
    print("\nPrivate employment average by president (thousands)")
    aveByPresident(priData, presidents)
    print("\nGovernment employment average by president (thousands)")
    aveByPresident(govData, presidents)

    # Plot data
    priPlot = plt.figure(1)
    plotGraph(priData, "Private", priPlot)
    govPlot = plt.figure(2)
    plotGraph(govData, "Government", govPlot)

    plt.show()

    
# Read in presidents from a file
def getPresidents(filename):
    presidents = []
    with open(filename, "r") as f:
        for line in f.readlines():
            tokens = [x.strip() for x in line.split(",")]
            years = [int(x.strip()) for x in tokens[1].split("-")]
            names = tokens[0].split()
            # Create list of Dictionaries for presidents
            presidents.append({"Name":names[len(names)-1], "Start":years[0], "Stop":years[1], "Party":tokens[2]})
    return presidents

# Read in data from a file
def getData(filename):
    data = {}
    with open(filename, "r") as f:
        keys = [x.strip() for x in f.readline().split(",")]
        for line in f.readlines():
            values = [int(x.strip()) for x in line.split(",")]
            # Create dictionary of dictionaries for data
            # Year             Month  : NumJobs
            data[values[0]] = {keys[i]:values[i] for i in range(1,len(keys))}
    return data

# Calculate average by month
def aveMonthly(data, presidents):
    # Calculate which years are democrats and which are republicans
    cratYears = [year for pres in presidents if pres["Party"] == "Democrat" for year in range(pres["Start"],pres["Stop"])]
    pubYears  = [year for pres in presidents if pres["Party"] == "Republican" for year in range(pres["Start"],pres["Stop"])]

    # Average the data by month
    cratAve = sum(data[year][month] for year in cratYears for month in data[year]) / (len(cratYears) * 12)
    pubAve = sum(data[year][month] for year in pubYears for month in data[year]) / (len(pubYears) * 12)

    # Ouput
    print("Democratic: {:-10.0f}".format(cratAve))
    print("Republican: {:-10.0f}".format(pubAve))

# Calculate data by president
def aveByPresident(data, presidents):
    # Format
    msgFormat = "{:<12s} {:>12s} {:>12s} {:>12s} {:>12s}"
    print(msgFormat.format("President","First Month","Last Month","Difference","Percentage"))
    msgFormat = "{:<12s} {:>12d} {:>12d} {:>12d} {:>11.1f}"

    for pres in presidents:
        # Output
        beg = data[pres["Start"]]["Jan"]
        end = data[pres["Stop"]-1]["Dec"]
        print(msgFormat.format(pres["Name"], beg, end, end-beg, (end/beg-1)*100))

# Plot a graph
def plotGraph(data, type, graph):
    # This is plotting the number of jobs over time in millions
    plt.plot(data.keys(), [sum([data[i][j] for j in data[i]])/10000 for i in data])
    title = "Number of "+type+" jobs over time in millions"
    plt.title(title)
    

main()