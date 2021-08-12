from Grid import Grid
import FileHandler


class Tetris:
    def loadInput(inputFilename):
        return FileHandler.parseInputFile(inputFilename)

    def runGames(sequences):
        heights = [Tetris.runGame(sequence) for sequence in sequences]
        return heights

    def runGame(sequence):
        grid = Grid()
        for instruction in sequence:
            grid.addPiece(Grid.shapes[instruction[0]], instruction[1])
        print(grid)
        print("")
        return grid.maxHeight()

    def saveHeights(heights, filename):
        FileHandler.saveOutput(heights, filename)


def main():
    sequences = Tetris.loadInput("input.txt")
    heights = Tetris.runGames(sequences)
    Tetris.saveHeights(heights, "output.txt")


if __name__ == "__main__":
    main()
