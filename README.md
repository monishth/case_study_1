# Case study 1

## Design

My first thought after seeing the task was to split it into more managable sections and tackle them 1 by 1. The file handling and the tetris engine can very clearly be split up so I decided to focus on the engine first. I then decided that python would be a good fit for this case study as it is very fast to develop with and it is easier to test ideas.

### Tetris engine

The engine itself can manage the execution of games and handling the instructions from the input while a grid class will manage the game logic.

#### Grid class

I decided to represent the empty grid as a list of lists filled with ```False```s as opposed to just empty lists as I felt that it could cause increased complexity when dealing with columns with gaps between their filled squares. 

I also decided that the inner lists in the grid representation will be columns as opposed to rows as the methods required will be less complex this way. 

There were a couple different ways of determining the position the piece lands at. Initially I was thinking to find the square on the piece that makes contact first using the heights of the columns in the map and the heights of each column in the piece. However I felt this may be a little too complex of a solution for a simplified engine, and landed on another solution. There are max 4 squares in a pieces so it would not be hard to go through each square at the bottom of the piece and place that square at the top of its column and put the rest of the squares around it and then check if any of these positions are already filled. There will always be only 1 height which works as there is no sideways movement. This was a much more readable and simple way to solve this problem.

I did realise that this method does not take into account if the leftmost squares are at a lower height but there are filled squares on the right that block it from falling. This is because the left most squares are defined first in the code and are checked first. I fixed this by sorting the order as the column with the largest height is checked first as this will prevent any overhanging filled squares from being overlooked

#### Tetris class

This class only needs to handle the execution of games and does not have any sort of state that needs to be manipulated or stored so I decided it would be a static class and it simply uses the FileHandler class to fetch instruction from the input file, runs the games and the writes the output to the specified output file.

### FileHandler class

This was a very very simple task in python as it really simplifies file handling with methods such as readLines and str.split which mean going from a file to a list of tuples that can be recognised as instructions is very simple
