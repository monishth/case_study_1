def parseInputFile(filename):
    with open(filename) as inputFile:
        rawLines = inputFile.readlines()
    stringInstructions = [line.split(",") for line in rawLines]
    instructions = [
        [(instruction[0], int(instruction[1])) for instruction in line]
        for line in stringInstructions
    ]
    return instructions


def saveOutput(outputList, filename):
    with open(filename, "w") as outputFile:
        outputFile.writelines([str(outputLine) + "\n" for outputLine in outputList])
