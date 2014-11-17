game_of_life_python
===================


This was a result of a code retreat. I'm not sure if this is the best ways for the game of life. I wrote this after coming home at the 
end of the day.
What I found is that a lot of people became somewhat obsessed with defining the grid. My solution focusing on defining the points. 
Each tick of the code updates a python dictionary with the active inactive points. 

Each key is a tuple for the x and y coordinates on the grid
and the value is 0 for a dead cell and 1 for a living cell. It only stores the cells that are active or where active.
It does not attempt to store a value for all items in and empty grid. 
