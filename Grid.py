class Grid:
    # Predefined shapes, represented by a square grid coordinate systemstarting at (0,0)
    # at the bottom left (even if it is empty)
    shapes = {
        "Q": ((0, 0), (0, 1), (1, 0), (1, 1)),
        "Z": ((0, 1), (1, 1), (1, 0), (2, 0)),
        "S": ((0, 0), (1, 0), (1, 1), (2, 1)),
        "T": ((0, 1), (1, 1), (2, 1), (1, 0)),
        "I": ((0, 0), (1, 0), (2, 0), (3, 0)),
        "L": ((0, 0), (0, 1), (0, 2), (1, 0)),
        "J": ((0, 0), (1, 0), (1, 1), (1, 2)),
    }

    # False for blank, True for filled square
    def __init__(self, rows=100, columns=10):
        # Initialises list of lists with False
        self.__grid = [[False for row in range(rows)] for col in range(columns)]

    def __str__(self):
        # Transformations of grid needed to print as a human would expect
        firstTransform = list(zip(*self.__grid))
        secondTransform = list(reversed(firstTransform))
        returnString = ""
        for row in secondTransform:
            # printed grid shows + for filled piece and - for empty square
            row = "".join(("+" if element else "-").center(3) for element in row)
            returnString += row + "\n"
        return returnString

    # The height (highest True in each column) is needed to know where the pieces come to rest
    # double underscore as this method should not be accesible from other modules
    def __columnHeight(self, colIndex):
        col = self.__grid[colIndex]
        if True in col:
            # Find index of last occurance of True (highest filled square in column) + 1 for height
            # This is done by reversing the list and finding the first occurance and then subtracting this from the length
            return len(col) - col[::-1].index(True)
        else:
            # If the column has no filled squares
            return 0

    # The task requires an output of the height of the remaining squares
    def maxHeight(self):
        return max(
            [self.__columnHeight(colIndex) for colIndex in range(len(self.__grid))]
        )

    # When a piece is placed if the specified rows are full this method will remove them and move the above pieces down 1
    def checkFullRow(self, rowIndex):
        row = [col[rowIndex] for col in self.__grid]
        if all(row):
            [self.removePiece(col, rowIndex) for col in self.__grid]

    # Removes piece from column safely (keeps grid size)
    def removePiece(self, column, index):
        column.pop(index)
        column.append(False)

    # Checks if a piece will fit in the grid without colliding with other pieces
    def isValidMove(self, shape):
        # If the piece is hitting the bottom of the grid, the false check is not enough as there are no falses and it will try
        # place the piece at the top of the grid
        if any(position[1] < 0 for position in shape):
            return False
        for position in shape:
            if self.__grid[position[0]][position[1]]:
                return False
        return True

    # This method handles the logic of the pieces landing and what position it lands in. The pieces
    # cannot move side to side, however the height they land at depends on the existing pieces on the map
    def addPiece(self, shape, leftColumnIndex):
        columnIndexes = [
            leftColumnIndex + relativeIndex
            for relativeIndex in list(set([position[0] for position in shape]))
        ]

        # Boundary check for columns, height is assumed to not exceed max height by the task
        if any(column >= len(self.__grid) and column < 0 for column in columnIndexes):
            raise IndexError("Input column is out of index")

        columnHeights = {
            columnIndex: self.__columnHeight(columnIndex)
            for columnIndex in columnIndexes
        }
        columnIndexes.sort(reverse=True, key=columnHeights.get)
        # After working out the height of each column that the piece is landing in, the piece is tried at each possible height
        # There is only 1 possible position so when the check returns true, those positions are assumed as the correct position
        for columnIndex in columnIndexes:
            # Within each column in the piece only the lowest square needs to be considered
            # So it is found here by finding the lowest square in the selected column
            anchorSquare = min(
                square
                for square in shape
                if square[0] == (columnIndex - leftColumnIndex)
            )
            # The new position of the squares within the piece are calculated around this new selected base position
            basePosition = (columnIndex, columnHeights[columnIndex])
            # This new list below contains the shape of the new piece with the absolute positions as opposed
            # to the relative coordinates that are predefined
            absoluteShape = [
                (
                    position[0] - anchorSquare[0] + basePosition[0],
                    position[1] - anchorSquare[1] + basePosition[1],
                )
                for position in shape
            ]

            # If this position for the piece is valid, then stop trying new heights
            if self.isValidMove(absoluteShape):
                break

        # Adds piece to determined position
        for position in absoluteShape:
            if self.__grid[position[0]][position[1]]:
                raise ValueError("position already filled")
            self.__grid[position[0]][position[1]] = True

        # Checks if any rows have been filled as these need to be removed
        for row in set([pos[1] for pos in absoluteShape]):
            self.checkFullRow(row)
