# Case study 1

## Design

My first thought after seeing the task was to split it into more managable sections and tackle them 1 by 1. The file handling and the tetris engine can very clearly be split up so I decided to focus on the engine first. I then decided that python would be a good fit for this case study as it is very fast to develop with and it is easier to test ideas.

### Tetris engine

The engine itself can manage the execution of games and handling the instructions from the input while a grid class will manage the game logic.

#### Grid class

I decided to represent the empty grid as a list of lists filled with ```False```s as opposed to just empty lists as I felt that it could cause increased complexity when dealing with columns with gaps between their filled squares. 

I also decided that the inner lists in the grid representation will be columns as opposed to rows as the methods required will be less complex this way. 

