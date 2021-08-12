from Grid import Grid


class Tetris:
    def loadInput(inputFilename):
        pass

    def runGames(sequences):
        pass

    def runGame(sequence):
        pass

    def saveHeights(heights, filename):
        pass


def main():
    grid = Grid()
    grid.addPiece(Grid.shapes["I"], 0)
    grid.addPiece(Grid.shapes["I"], 4)
    grid.addPiece(Grid.shapes["Q"], 8)
    print(grid, grid.maxHeight())


if __name__ == "__main__":
    main()
